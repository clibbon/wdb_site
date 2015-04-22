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

class AppError(Exception):
    """ Class for all my errors from this app"""
    pass

# Main function which handles texts
def handleMessage(request):
    resp = twilio.twiml.Response()
    # Try to read the text and the sender
    try:
        msgText = request.POST.__getitem__('Body')
        msgSender = request.POST.__getitem__('From')
    except Exception as e:
        print e
    
    # Try to save the message
    try:
        saveMsgHistory(msgText, msgSender)
    except AppError as e:
        print e
        print 'Failed to save message'
    except Exception as e:
        print e
    
    # Check for keywords
    keyWord = getKeyWord(msgText)
    if keyWord == 'correct':
        try:
            detailDict = getDetailsFromCookie(request)
            # Add to database
            warCreated, pId, cId = addToDatabase(detailDict,msgSender)
            if warCreated:
                resp.message(generateConfirmationReply(pId, cId))
            else:
                resp.message(existingWarrantyReply(pId, cId))
        except Exception as e:
            print e
            print sys.exc_traceback.tb_lineno
    elif keyWord == 'retry':
        try:
            detailDict = getStructuredTextInfo(msgText)
        except Exception as e:
            print e
    else:
        # Parse the text
        try:
            details = getTextInfo(msgText)
            resp.message(generateSuccessReply(details))
            # Store cookie
            resp = addDetailsToCookie(details,resp)
        except AppError as e:
            print e
            resp.message(
                        'Sorry your information could not be read. '
                        'Please reply with the word RETRY and your details '
                        'in this order:\n'
                        'Forename Surname SerialNo ModelNo Region')
        except Exception as e:
            print e
            
    print resp
    return resp



def getTextInfo(message, debug=False):
    # Remove all non alpha numeric characters
    message = re.sub(r'([^\s\w]|_)+', '', message) 
    # Split the text up
    words = message.split()
    # Identify model no and serial no
    serNum, modelNum, words = findModelNums(words)
    if debug:
        print "After identification of serial/model num"
        print serNum, modelNum, words
    # Find the region
    region = findRegion(message.lower())
    if debug:
        print "Region found is %s" % region
    # Remove non-Proper-nouns
    properNouns = selectProperNouns(words)
    # Remove any region matches
    words = removeRegions(properNouns,region)
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
    words = message.split()
    detailDict = {
    'ForeName' : words[0],
    'SurName' : words[1],
    'SerNo' : words[2],
    'ModNo' : words[3],
    'Region': words[4]
    }
    return detailDict

def retryReply():
    return 'Please enter you details in this order, separated by spaces. Forename' + \
            ' SurName SerialNo ModelNo Region'
        

# Function adds details to the response cookie
def addDetailsToCookie(details,response):
    response.set_cookie("ForeName", value=details['ForeName'])
    response.set_cookie("SurName", value=details['SurName'])
    response.set_cookie("SerNo", value=details['SerNo'])
    response.set_cookie("ModNo", value=details['ModNo'])
    response.set_cookie("Region",value=details['Region'])
    return response

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

# Find the alphanumeric values in the input string
def findModelNums(words):
    possibleMatches = [] 
    for word in words:
        if not re.match("^[A-Za-z]+$", word): 
            possibleMatches.append(word) 
    
    # Check for errors
    if len(possibleMatches) > 2:
        print possibleMatches
        raise AppError(
            'Could not identify serial number/model number,'
            ' too many alphanumeric words')
    elif len(possibleMatches) < 2:
        raise AppError(
            'To few serial number/model number '
            'matches found')
    
    # Find which is longest
    matchLengths = [len(i) for i in possibleMatches]
    
    # Check lengths aren't identical
    if matchLengths[0]==matchLengths[1]:
        raise AppError(
            'Could not distinguish serial number as same '
            'length as model num')
    
    # Get the index of the serial
    idx = matchLengths.index(max(matchLengths))
    
    serNum = possibleMatches.pop(idx)
    modelNum = possibleMatches[0]
    # Remove words from list
    words.remove(serNum)
    words.remove(modelNum)
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
    return words[0]

# Receipt on successful generation of new warranty
def generateConfirmationReply(pId, cId):
    return 'Warranty confirmed'
    
# Reponsd to the case where there is an existing warranty
def existingWarrantyReply(pId, cId):
    return 'Warranty already exists'
    
# Generate a response to a successful registry
def generateSuccessReply(detailDict):
    
    msgText = (
        'Thankyou for registering. Your details are: \n'
        'Name - %(ForeName)s %(SurName)s, \n'
        'SerNo -  %(SerNo)s, \n' 
        'Model %(ModNo)s, \n'
        'Region %(Region)s. \n'
        'If these are correct, reply CORRECT to receive your receipt. If wrong'
        ' reply RETRY.'
        % detailDict)
    return msgText