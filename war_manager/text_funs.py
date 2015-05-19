# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 11:06:16 2015

Functions for parsing text and saving it in django

@author: alex
"""

from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from lists import regions
import re
from nltk import pos_tag
import twilio.twiml
from db_funs import saveMsgHistory,addToDatabase
import sys
from django.http.response import HttpResponse
from war_manager.models import Product, ProductModel
import traceback

# Messages
retryReply = ('Sorry your information could not be read. '
             'Please reply with the word RETRY and your details '
             'in this order:\n'
             'Forename Surname SerialNo ModelNo Region')


class AppError(Exception):
    """ Class for all my errors from this app"""

# Main function which handles incoming text messages
def handleMessage(request):
    resp = twilio.twiml.Response()
    # Read the text and get the sender information
    try:
        msgText = request.POST.__getitem__("Body")
        msgSender = request.POST.__getitem__("From")
    except Exception as e:
        print(traceback.format_exc())
        raise AppError("Couldn't read msg information from POST. Could not find POST[{}]".format(e))
    
    # Save the message in the history folder
    try:
        saveMsgHistory(msgText, msgSender)
    except AppError as e:
        print(traceback.format_exc())
        raise AppError("Couldn't save message".format(e))
    except Exception as e:
        print('Oh, something unexpected went wrong')
        print(traceback.format_exc())
    
    # Check for keywords
    keyWord = getKeyWord(msgText)
    if keyWord == 'correct':
        # Attempt to register the warranty
        try:
            detailDict              = getDetailsFromCookie(request)
            warCreated, cId, pId    = addToDatabase(detailDict,msgSender)
            if warCreated:
                resp.message(generateConfirmationReply(pId, cId))
            else:
                resp.message(existingWarrantyReply(pId, cId))
        except Exception as e:
            print(traceback.format_exc())
            raise AppError()
    elif keyWord == 'retry':
        # Read data in a structured format
        try:
            detailDict = getStructuredTextInfo(msgText)
            resp = addDetailsToCookie(detailDict,HttpResponse(resp))
        except Exception as e:
            print(traceback.format_exc())
            raise AppError('Could not read structured text info')
            resp.message = ("Your information couldn't be read, ADD LOGIC HERE...")
    else:
        # Parse the text
        try:
            detailDict  = getTextInfo(msgText)
            resp.message(generateSuccessReply(detailDict))
            resp        = addDetailsToCookie(detailDict,HttpResponse(resp))
        except AppError as e:
            print(traceback.format_exc()) 
            raise AppError("Text info couldn't be read. Error {}".format(e))
            resp.message(retryReply)
        except Exception as e:
            print(traceback.format_exc()) 
            raise       
    return resp



def getTextInfo(message, debug=False):
    ''' Parses the information in the message 
    and returns a dictionary containing the 
    customer and product information.
    '''
    # Remove all non alpha numeric characters
    message = re.sub(r'([^\s\w]|_)+', '', message) 
    # Split the text up
    words = message.split()
    # Identify model no and serial no by matching to 
    # existing entries in the database.
    serNum, modelNum, words = findModelNums(words)
    if debug:
        print "After identification of serial/model num"
        print serNum, modelNum, words
    # Find the region
    region = findRegion(message.lower())
    if debug:
        print "Region found is %s" % region
    # Remove non-Proper-nouns
    #properNouns = selectProperNouns(words) Removed 19/05/15 as it tends to cause problems with matching names to real words
    # Remove any region matches
    words = removeRegions(words,region)
    # Find the names
    forename, surname = getNames(words)
    
    detailDict = {
    'ForeName' : forename,
    'SurName' : surname,
    'SerNo' : serNum,
    'ModNo' : modelNum,
    'Region': region
    }
    return detailDict

# Function to read the second attempt by parsing individual bits
def getStructuredTextInfo(message):
    '''
    Note that we go from the 2nd to last words, as the first word 
    is always RETRY.
    '''
    words = message.split()
    detailDict = {
    'ForeName' : words[1],
    'SurName' : words[2],
    'SerNo' : words[3],
    'ModNo' : words[4],
    'Region': words[5]
    }
    return detailDict
        

# Function adds details to the response cookie
def addDetailsToCookie(details,response):
    response.set_cookie("ForeName", value=details['ForeName'])
    response.set_cookie("SurName", value=details['SurName'])
    response.set_cookie("SerNo", value=details['SerNo'])
    response.set_cookie("ModNo", value=details['ModNo'])
    response.set_cookie("Region",value=details['Region'])
    return response

# Reads information from cookie
def getDetailsFromCookie(request):
    detailDict = {
    'ForeName' : request.COOKIES.get('ForeName',''),
    'SurName' : request.COOKIES.get('SurName',''),
    'SerNo' : request.COOKIES.get('SerNo',''),
    'ModNo' : request.COOKIES.get('ModNo',''),
    'Region': request.COOKIES.get('Region',0)
    }
    
    # Check that we've still got the cookie
    if detailDict['ForeName']=='':
        raise AppError(
        'Cookie has either timed out, or could not be '
        'loaded properly')
    return detailDict

# Find the alphanumeric values in the input string, and match them up to existing 
# model and serial numbers
def findModelNums(words):
    '''
    Returns sernum, modelnum, and words.
    ser_num is the serial number found in the database
    model_num is the model found in the database
    words are the remaining words
    '''
    # All alphanumeric words are possible matches
    possibleMatches = [] 
    for word in words:
        if not re.match("^[A-Za-z]+$", word): 
            possibleMatches.append(word)
    # Do we have enough to search for model and sernum
    if len(possibleMatches) < 2:
        raise AppError(
            'To few serial number/model number '
            'matches found')
    # First try to match the model (by short code)
    possibleModelNums = []
    for match in possibleMatches:
        try:
            ProductModel.objects.get(model=match)
            possibleModelNums.append(match)
        except ProductModel.DoesNotExist:
            pass
    # Check that we have exactly one model
    if len(possibleModelNums) > 1:
        raise AppError(
            'Multiple model matches found'
            )
    elif len(possibleModelNums) < 1:
        raise AppError(
            'No model matches found')
    modelNum = possibleModelNums[0]
    possibleMatches.pop(possibleMatches.index(modelNum))
    words.pop(words.index(modelNum))
    # Now search for serial numbers
    serNumMatches = []
    for sernum in possibleMatches:
        try:
            print sernum
            Product.objects.get(ser_num=sernum,model__model=modelNum)
            serNumMatches.append(sernum)
        except Product.DoesNotExist:
            pass
    # Check we have only one serial number
    if len(serNumMatches) > 1:
        raise AppError(
            'Too many serial numbers found. Numbers were {}'.format(sernum)
            )
    elif len(serNumMatches) < 1:
        raise AppError(
            'No serial number matches found'
            )
    serNum = serNumMatches[0]
    words.pop(words.index(serNum))
    return (serNum, modelNum, words)    

# Return the names from the list of proper nouns
def getNames(properNouns):
    if len(properNouns) > 2:
        raise AppError('Too many names discovered')
    elif len(properNouns) < 2:
        raise AppError('Only one name discovered')
    first_name = properNouns[0]
    first_name = ("".join([first_name[0].upper(),first_name[1:len(first_name)]]))        
    surname = properNouns[1]
    surname = ("".join([surname[0].upper(),surname[1:len(surname)]]))
    return first_name,surname
    
# Find the words matching the region name
def findRegion(message,sens=70):
    ''' message is a string of the entire message (with punctuation removed)
    sens is the sensitivity of the fuzzy matcher. Lower = less specific '''
    ratio = []
    # String match region names
    for region in regions:
        ratio.append(fuzz.partial_ratio(message,region.lower()))
    
    if max(ratio) > sens:
        idx = ratio.index(max(ratio))
    else:
        raise AppError('Could not identify a region')
    return regions[idx]

# Selects only proper nouns from the word list. 
''' This function isn't used since it isn't great at picking out the name.
'''
def selectProperNouns(words):
    properNouns = []
    taggedWords = pos_tag(words)
    for (word, kind) in taggedWords:
        if kind == 'NNP':
            properNouns.append(word)
    return properNouns
    
# Remove found regions from the words list
def removeRegions(words, region, sens=70):
    ''' Again sensitivity is the sensitivity of the fuzzy matcher
    and words a list of the words in the message'''
    # See if region consists of two words
    reg_words = region.split()
    newList = []
    for word in words:
        temp = []
        for region in reg_words:
            temp.append(fuzz.partial_ratio(word.lower(),
                                           region.lower()))
        if max(temp) < sens:
            newList.append(word)
    return newList
        
        
        
# Function extracts keywords from the message (hint: it's the first word)
def getKeyWord(msgText):
    words = msgText.split()
    return words[0].lower()

# Receipt on successful generation of new warranty
def generateConfirmationReply(pId, cId):
    # Get status of product and warranty
    print pId
    p = Product.objects.get(pid=pId)
    print 'got this far'
    print p
    if p.model.is_verified:
        filler = ' is '
    else:
        filler = ' is not '
    msgText = (
        'Warranty confirmed! \n'
        'Registered %s \n'
        'Expires %s \n'
        'Product %s verified by lighting Africa'
        % (p.warranty.reg_date, p.warranty.exp_date, filler))
    print msgText
    return msgText
    
# Reponsd to the case where there is an existing warranty
def existingWarrantyReply(pId, cId):
    return 'Warranty already exists'
    
# Generate a response to a successful registry
def generateSuccessReply(detailDict):
    
    msgText = (
        'Thankyou for registering. Your details are: \n'
        'Name - %(ForeName)s %(SurName)s, \n'
        'SerNo -  %(SerNo)s, \n' 
        'Model - %(ModNo)s, \n'
        'Region - %(Region)s. \n'
        'If these are correct, reply CORRECT to receive your receipt. If wrong'
        ' reply RETRY.'
        % detailDict)
    return msgText