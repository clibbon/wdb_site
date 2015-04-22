from django.contrib import admin
from war_manager.models import (Customer, Product, ProductImport,
                                ProductModel, Importer, Warranty,
                                Message)

class WarrantyInline(admin.StackedInline):
    model = Warranty
    extra = 1

class ProductInline(admin.StackedInline):
    model = Product
    extra = 1

class MessagesInline(admin.TabularInline):
    model = Message
    extra = 5

# Define field views
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('__str__','mob_number','region','profile')
    fieldsets = [
        ('Name',      {'fields':
                     ['first_name','last_name']}),
        ('Details', {'fields':
                     ['mob_number','region']})
                 ]
    inlines = [WarrantyInline,MessagesInline]
                 
class ProductImportAdmin(admin.ModelAdmin):
    list_display = ('pid', 'imp_date')
    
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('model','mid', 'is_verified')
    
class ImporterAdmin(admin.ModelAdmin):
    list_display = ('identity','iid')
    
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ('reg_date','exp_date')
    list_filter = ['reg_date']
    
    inlines = [ProductInline]

class MessageAdmin(admin.ModelAdmin):
    list_display = ('date_received', 'mob_number', 'msg_text')
    list_filter = ['date_received']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('ser_num',)

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImport, ProductImportAdmin)
admin.site.register(ProductModel, ProductModelAdmin)
admin.site.register(Importer, ImporterAdmin)
admin.site.register(Warranty, WarrantyAdmin)
admin.site.register(Message, MessageAdmin)