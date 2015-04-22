from django import forms
from war_manager.models import Product, ProductModel
# Forms for website

class ImportForm(forms.ModelForm):
    ser_num = forms.CharField(max_length=30, required=True)
    model = forms.ModelChoiceField(queryset=ProductModel.objects.all(),empty_label=None)
    class Meta:
        model = Product
        fields = ['ser_num','model']
    def __init__(self,*args,**kwargs):
        if kwargs.get('instance'):
            email = kwargs['instance'].email
            kwargs.setdefault('initial', {})['confirm_email'] = email
        return super(ImportForm, self).__init__(*args, **kwargs)
    
    # Check that the two emails match. These steps are performed after the initial
    # data cleaning that is performed by Django itself
    def clean(self):
        if (self.cleaned_data.get('email') !=
            self.cleaned_data.get('confirm_email')):

            return self.cleaned_data
        
        
