from django.contrib import admin
from war_manager.models import (Customer, Product,
                                ProductModel, Importer, Warranty,
                                Message)
from django.forms.models import BaseInlineFormSet

class WarrantyInline(admin.StackedInline):
    model = Warranty
    extra = 1

class ProductInline(admin.StackedInline):
    model = Product
    extra = 1

class MessageInLineFormSet(BaseInlineFormSet):
    def get_queryset(self) :
        qs = super(MessageInLineFormSet, self).get_queryset()
        if qs.count() <= 5:
            return qs
        else:
            return qs[ qs.count()-6: qs.count()-1]
    
class MessagesInline(admin.TabularInline):
    model = Message
    formset = MessageInLineFormSet
    extra  = 0
    class Meta:
        ordering = ('-date_received',)

# Define field views
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('cid','__str__','mob_number','region','profile')
    fieldsets = [
        ('Name',      {'fields':
                     ['first_name','last_name']}),
        ('Details', {'fields':
                     ['mob_number','region']})
                 ]
    inlines = [WarrantyInline,MessagesInline]
    
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('model','mid', 'is_verified')
    
class ImporterAdmin(admin.ModelAdmin):
    list_display = ('identity','iid')
    
class WarrantyAdmin(admin.ModelAdmin):
    list_display = ('wid','reg_date','exp_date')
    list_filter = ['reg_date']
    
    inlines = [ProductInline]

class MessageAdmin(admin.ModelAdmin):
    list_display = ('date_received', 'mob_number', 'msg_text')
    list_filter = ['date_received']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('ser_num','model',)

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductModel, ProductModelAdmin)
admin.site.register(Importer, ImporterAdmin)
admin.site.register(Warranty, WarrantyAdmin)
admin.site.register(Message, MessageAdmin)