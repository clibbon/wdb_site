from django import forms
from war_manager.models import Product, ProductModel, Importer
from django.core.exceptions import ValidationError
# Forms for website

class ImportForm(forms.ModelForm):
    ser_num = forms.CharField(max_length=30, required=True)
    model = forms.ModelChoiceField(queryset=ProductModel.objects.all(),empty_label=None)
    class Meta:
        model = Product
        fields = ['ser_num','model']
    
    # Once the form has been submitted, try and add this to the database
    # along with everything else
    def clean(self):
        if Product.objects.filter(ser_num=self.cleaned_data.get('ser_num')).exists():
            raise ValidationError('Serial number already exists')
            return self.cleaned_data
        

        
