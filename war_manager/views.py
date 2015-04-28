from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView
from django.contrib.auth import authenticate, login
from text_funs import handleMessage
from war_manager.models import Product, Importer, Customer, ProductModel
from django_twilio.decorators import twilio_view
from war_manager.forms import ImportForm
from war_manager.db_funs import createProductImport
from django.views.generic.edit import UpdateView

# Create your views here.
class Home(TemplateView):
    print 'received'
    template_name = 'homepage.html'

class TestView(TemplateView):
    return HttpResponse("I'm a test page")

#### Views for handling product models ####
# Show all models in a list
class ModelList(ListView):
    model = ProductModel
    template_name='model_list.html'
    def get_queryset(self):
        return ProductModel.objects.all()

# Form to create a new model
class ModelCreate(CreateView):
    model = ProductModel
    template_name='model_list.html'
    def get_success_url(self):
        return reverse('model-list')
    def get_context_data(self, **kwargs):
        context = super(ModelCreate, self).get_context_data(**kwargs)
        context['action'] = reverse('model-new')
        return context    

# Form to update existing models
class ModelUpdate(UpdateView):
    model = ProductModel
    template_name='model_list.html'
    def get_success_url(self):
        return reverse('model-edit')
    def get_context_data(self, **kwargs):
        context = super(ModelCreate, self).get_context_data(**kwargs)
        context['action'] = reverse('model-edit',
                                    kwargs={'pk': self.get_object().id})
        return context

#### Views for importing products #### 
# Home page   
class ImportProductView(CreateView):
    form_class = ImportForm
    model = Product
    template_name = 'import.html'
    
    def get_success_url(self):
        return reverse('importer-home')
    
    # Get the context
    def get_context_data(self, **kwargs):
        
        context = super(ImportProductView, self).get_context_data(**kwargs)
        # Adding my own context
        user = self.request.user
        try:
            importer = Importer.objects.get(user_id__username=user)
            context['Products'] = Product.objects.filter(importer=importer)[:5]
            context['action'] = reverse('importer-home')
        except Importer.DoesNotExist:
            context['action'] = reverse('importer-home')
        return context

# Handl
def addProductToDatabase(request):
    
    try:
        isNewProduct = createProductImport(request)
        if isNewProduct:
            return redirect('importer-home')
        else:
            return HttpResponse('Product already imported')
    except Importer.DoesNotExist:
        return HttpResponse('User %s does not have permission to import products' % request.user)

#### Useful views ####
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
    print request
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

#### Customer search page views   
# Not sure if required, but splash page     
class ManagerHome(TemplateView):
    template_name ='manage.html'
        
    def get_success_url(self):
            
        return reverse('manager-home')
    
    # Get the context
    def get_context_data(self, **kwargs):
        
        context = super(ManagerHome, self).get_context_data(**kwargs)
        context['action'] = reverse('search-page')
        return context

# View info on individual customers
def customerDetail(request,cust_id):

    return render(request,'customer_view.html',
           {'Customer' : Customer.objects.get(pk=cust_id),
            'Products' : Product.objects.filter(warranty__customer__pk=cust_id)
            })
    
# The single search page renders results
def SearchPage(request):
    print request.GET
    qs = Product.objects.all()
    # If something entered in the name field
    if 'ser_num' in request.GET:
        if request.GET['ser_num'] != '':
            qs = qs.filter(ser_num=request.GET['ser_num'])
    if 'first_name' in request.GET:
        if request.GET['first_name'] != '':
            qs = qs.filter(warranty__customer__first_name=request.GET['first_name'])
    if 'last_name' in request.GET:
        if request.GET['last_name'] != '':
            qs = qs.filter(warranty__customer__last_name=request.GET['last_name']) 
                
    # Now create a new object list to display the results
    return render(request,'manage.html',{'Results': qs})
    
#### Views to handle incoming text messages #### 
@twilio_view
def text_receiver(request):
    try:
        return handleMessage(request)
    except Exception as e:
        print e
        return HttpResponse('There was an error')
    
    
    
    
    
    
    
    
    
    
    
# Blah