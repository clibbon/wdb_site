from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from lists import regions
from django.core.urlresolvers import reverse

# Customer model - the end user
class Customer(models.Model):
    cid         = models.AutoField(primary_key=True)  # Field name made lowercase.
    first_name  = models.CharField(max_length=30, blank=False, default='None')
    last_name   = models.CharField(max_length=30, blank=False, default='Set')
    mob_number  = models.CharField(max_length=24, blank=True, null=True)
    region      = models.IntegerField(blank=True, null=True)
    profile     = models.ForeignKey(User, default = 1)
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    def region_name(self):
        return regions[self.region]
        
    class Meta:
        db_table = 'customer'
        verbose_name_plural = 'customers'
        
# Importer company - allows multiple users to be attached   
class Importer(models.Model):
    iid         = models.AutoField(primary_key=True)  # Field name made lowercase.
    user_id     = models.ForeignKey(User)
    identity    = models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.identity

# Model type 
class ProductModel(models.Model):
    mid         = models.AutoField(primary_key=True)  # Field name made lowercase.
    model       = models.CharField(max_length=20, blank=True)
    is_verified = models.BooleanField(default=False)
    war_length  = models.IntegerField(default=0, blank=True)
    long_name   = CharField(max_length=60, null=True)
    
    def __str__(self):
        return self.model
    def get_absolute_url(self):
        return reverse('model-details',kwargs={'pk':self.id})

# Warranty object, sits between product and customers
class Warranty(models.Model):
    wid         = models.AutoField(primary_key=True)  # Field name made lowercase.
    reg_date    = models.DateField(blank=True, null=True)
    exp_date    = models.DateField(blank=True, null=True)
    customer    = models.ForeignKey(Customer, null=True)
    
    def __str__(self):
        return 'exp: ' + str(self.exp_date)
    
    class Meta:
        verbose_name_plural = 'Warranties'

# An individual instance of a product        
class Product(models.Model):
    pid         = models.AutoField(primary_key=True)  # Field name made lowercase.
    ser_num     = models.CharField(max_length=30, blank=False)
    model       = models.ForeignKey(ProductModel)
    warranty    = models.ForeignKey(Warranty, null=True)
    imp_date    = models.DateField(blank=True, null=True)
    importer    = models.ForeignKey(Importer, null=True, blank=True)
    
    def __str__(self):
        return self.ser_num
    
    class Meta:
        ordering = ['-pid']

# The database of messages received    
class Message(models.Model):
    id          = models.AutoField(primary_key=True)
    msg_text    = models.CharField(max_length=511)
    date_received = models.DateTimeField(blank=True, null=True)
    mob_number  = models.CharField(max_length=24, blank=True)
    customer    = models.ForeignKey(Customer, null=True)
    
    def __str__(self):
        return self.msg_text
    
    class Meta:
        ordering = ['-id']
    
    
    
    
    
