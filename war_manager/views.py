from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login

# Create your views here.
class Home(TemplateView):
    print 'received'
    template_name = 'homepage.html'
    
class Placeholder(TemplateView):
    print 'at placeholder'
    template_name = 'placeholder.html'
    
# Receive login attempt and redirect to another section
def login_redirect(request):
    print 'I got here'
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        print 'And also here'
        if user.is_active:
            #if user.group
            login(request, user)
            # Redirect to a success page.
            l = []
            for g in request.user.groups.all():
                l.append(g.name)
            print l
            return HttpResponse('Success')
        else:
            # Return a 'disabled account' error message
            print 'Oh dear'
    else:
        # Return an 'invalid login' error message.
        print 'Oh dear'
    
    HttpResponse('Success')
        
    