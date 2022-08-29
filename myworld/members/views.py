
# Create your views here.

# Django views are Python functions that takes http requests and
# returns http response, like HTML documents.

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())
