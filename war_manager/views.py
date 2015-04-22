from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from text_funs import handleMessage
from war_manager.models import Product
from django_twilio.decorators import twilio_view
from war_manager.forms import ImportForm
from war_manager.db_funs import createProductImport

# Create your views here.
class Home(TemplateView):
    print 'received'
    template_name = 'homepage.html'

class TestView(CreateView):
    model = Product
    

class ImportProductView(CreateView):
    form_class = ImportForm
    model = Product
    template_name = 'import.html' 
    #form_class = forms.ContactForm
    
    def get_success_url(self):
        return reverse('importer-home')
    
    def get_context_data(self, **kwargs):
        
        context = super(ImportProductView, self).get_context_data(**kwargs)
        context['action'] = reverse('importer-home')
        
        return context

def addProductToDatabase(request):
    
    createProductImport(request)

class Placeholder(TemplateView):
    print 'at placeholder'
    template_name = 'placeholder.html'

# Simply sends user to appropriate place
def user_redirect(request):
    if request.user.groups.filter(name='importer').exists():
        return redirect('importer-home')
    elif request.user.groups.filter(name='manager').exists():
        return redirect('manager-home')
    elif request.user.groups.filter(name='customer').exists():
        print 'Not using customers yet'
        return redirect('home')
            
# Receive login attempt and redirect to another section
def login_redirect(request):
    print 'I got here'
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        print 'And also here'
        if user.is_active:
            #if user.group
            login(request, user)
            # Redirect to a success page.
            if user.groups.filter(name='importer').exists():
                return redirect('importer-home')
            elif user.groups.filter(name='manager').exists():
                return redirect('manager-home')
            elif user.groups.filter(name='customer').exists():
                print 'Not using customers yet'
                return redirect('home')
            else:
                return HttpResponse("You don't belong to any groups - check with the administrator")
        else:
            # Return a 'disabled account' error message
            print 'TODO - deal with disabled accounts'
    else:
        # Return an 'invalid login' error message.
        print 'TODO - deal with login errors'
    
    HttpResponse('Success')
        
class ManagerHome(TemplateView):
    template_name ='manage.html'
    
class ImportHome(TemplateView):
    template_name ='import.html'

    def get_context_data(self, **kwargs):
        context = super(ImportHome, self).get_context_data(**kwargs)
        #context['latest_imports'] = ProductImport.objects.filter(__Importer__)[:5]
        return context
    
# Here we handle the incoming text messages
@twilio_view
def text_receiver(request):
    try:
        return handleMessage(request)
    except Exception as e:
        print e
        return HttpResponse('There was an error')
    
    
    
    
    
    
    
    
    
    
    
# Blah