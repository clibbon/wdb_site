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

# Function to save incoming message to msg log
def saveMsgHistory(message, sender):
    '''Attempts to save the message, and associate it with as customer
    If no customer exists already, then make a new one and raise that tag'''
    print 'I got to saveMsgHistory'
    c, isNew = Customer.objects.get_or_create(mob_number=sender)
    c.message_set.create(msg_text = message, 
                                  date_received = datetime.now().date(), 
                                  mob_number = sender)
    return isNew
    
# Function checks if a customer exists, and if not creates one
def checkCustomer(detailDict,mob_num):
    c, newCustomer = Customer.objects.get_or_create(mob_number = mob_num,)
    
    if newCustomer:
        c.first_name    = detailDict['ForeName']
        c.last_name     = detailDict['SurName']
        c.region        = regions.index(detailDict['Region'])
        print 'New customer created'
    
    return c.cid
    
# Function checks if a product exists
def checkProduct(detailDict):
    m = ProductModel.objects.get(model = detailDict['ModNo'])
    p, newProduct = Product.objects.get_or_create(
        ser_num = detailDict['SerNo'],
        model = m)
    
    if newProduct:
        print 'New product created'
    return p.pid

# Function checks if a warranty exists
def warrantyExists(cId,pId):
    return Warranty.objects.filter(product__pid=pId).exists()
        

# Function attempts to add warranty to the database. Returns a
# message string, either a receipt, or 
def addToDatabase(detailDict,mob_num):
    '''Function will return True if successful
    otherwise will return false'''
    
    # Check if customer and/or warranty already exist
    cId = checkCustomer(detailDict,mob_num)
    pId = checkProduct(detailDict)
    
    # Check if a warranty exists already
    if warrantyExists(cId,pId):
        return [False, cId, pId]
    else:
        print 'Tried creating warranty'
        createWarranty(detailDict,cId,pId)
        print 'Created warranty'
        return [True, cId, pId]

# Function creates a warranty. Uses the current time and date. Assume they're
# all 2 years for now. 
def createWarranty(detailDict, cId, pId):
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
    print 'I got into getWarrantyEnd function'
    tempTime = time.mktime(time.strptime(startDate,'%Y-%m-%d'))
    print 'This line ran'
    tempTime = time.strftime('%Y-%m-%d', time.localtime(tempTime +
                                            3600*24*7*52*yearsValid))
    
    return tempTime

def createProductImport(request):
    ser_num     = request.POST['ser_num']
    model_pk    = request.POST['model'] # gives the model pk
    print request.user
    importer    = Importer.objects.filter(user_id__username=request.user)
    p, isNew = Product.objects.get_or_create(ser_num = ser_num,
                                             model = ProductModel.objects.get(pk=model_pk),
                                             importer = importer
                                             )
    print 'I made it'
    