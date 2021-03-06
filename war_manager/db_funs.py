# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:46:08 2015

@author: alex

Functions for saving the data to the database in django,
 and creating the reply message.
"""
from datetime import datetime
from war_manager.models import (Customer, Product, Warranty, ProductModel, Importer)
from lists import regions
import time
from django.utils import timezone

# Function to save incoming message to msg log
def saveMsgHistory(message, sender):
    '''Attempts to save the message, and associate it with as customer
    If no customer exists already, then make a new one and raise that tag'''
    c, isNew = Customer.objects.get_or_create(mob_number=sender)
    c.message_set.create(msg_text = message, 
                                  date_received = timezone.now(), 
                                  mob_number = sender)
    return isNew



# Function checks if a customer exists, and if not creates one
def checkCustomer(detailDict,mob_num):
    '''
    Returns the customers pk. Need to check whether the customer already exists, 
    and whether they've already been created through the message recorder.
    '''
    c, newCustomer = Customer.objects.get_or_create(mob_number = mob_num,)
    if newCustomer or c.first_name == 'None':
        c.first_name    = detailDict['ForeName']
        c.last_name     = detailDict['SurName']
        c.region        = regions.index(detailDict['Region'])
        c.save()
        
    return c.cid


    
# Function checks if a product exists
def checkProduct(detailDict):
    m = ProductModel.objects.get(model = detailDict['ModNo'])
    p, newProduct = Product.objects.get_or_create(
        ser_num = detailDict['SerNo'],
        model = m)

    return p.pid




# Function checks if a warranty exists
def warrantyExists(cId,pId):
    return Warranty.objects.filter(product__pid=pId).exists()
        


# Function attempts to add warranty to the database. Returns a
# message string, either a receipt, or 
def addToDatabase(detailDict,mob_num,verbose=False):
    '''Function will return True if successful
    otherwise will return false'''
    
    # Check if customer and/or warranty already exist
    cId = checkCustomer(detailDict,mob_num)
    pId = checkProduct(detailDict)
    
    # Check if a warranty exists already
    if warrantyExists(cId,pId):
        return [False, cId, pId]
    else:
        if verbose: print 'Tried creating warranty'
        createWarranty(detailDict,cId,pId)
        if verbose: print 'Created warranty, cid=%s, pid=%s' % (cId, pId,)
        return [True, cId, pId]



# Function creates a warranty. Uses the current date.
def createWarranty(detailDict, cId, pId):
    ''' It should be impossible to get this far is p and c
        don't already exist.   
    '''
    p = Product.objects.get(pid=pId)
    c = Customer.objects.get(cid=cId)
    # Get warranty length
    war_len = int(ProductModel.objects.filter(product__pid=pId)[0].war_length)
    w = Warranty.objects.create(
        reg_date = datetime.now().date(),
        exp_date = getWarrantyEnd(str(datetime.now().date()),war_len))
    c.warranty_set.add(w)
    w.product_set.add(p)
    
    return True


    
def getWarrantyEnd(startDate,yearsValid):
    """ Adds a number of years onto the given date. 
        Input string
        Output timedate.date structure
        
        # Demonstration
        date = '2010-1-1'
        warrantyYears = 10
        print date
        print getWarrantyEnd(date,warrantyYears)
    """
    tempTime = time.mktime(time.strptime(startDate,'%Y-%m-%d'))
    tempTime = time.strftime('%Y-%m-%d', time.localtime(tempTime +
                                            3600*24*7*52*yearsValid))
    
    return tempTime




def createProductImport(request):
    '''
    Function called when an importer attempts to add a product. If the product already 
    exists will flag an error. 
    '''
    # Read info about import request - who's trying to import
    importer    = Importer.objects.get(user_id__username=request.user)
    ser_num     = request.POST['ser_num']
    model_pk    = request.POST['model'] # gives the model pk
    hasAnotherImporter = False          # A check that we haven't already imported the product
    # Attach and create the product if it doesn't exist already
    try:
        p = Product.objects.get(ser_num = ser_num,
                            model = ProductModel.objects.get(pk=model_pk),
                            )
        if p.importer is '':
            p.importer = importer
            p.imp_date = datetime.now().date()
            p.save()
        else:
            hasAnotherImporter = True
            print "database error in CreateProductImport"
        isNew = False
    except Product.DoesNotExist:
        Product.objects.create(ser_num  = ser_num,
                               model    = ProductModel.objects.get(pk=model_pk),
                               importer = importer,
                               imp_date = datetime.now().date()
                               )
        isNew = True
         
    return isNew, hasAnotherImporter
    