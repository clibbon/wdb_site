from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView


# Create your views here.
class Home(TemplateView):
    print 'received'
    template_name = 'homepage.html'
    
class Placeholder(TemplateView):
    print 'at placeholder'
    template_name = 'placeholder.html'