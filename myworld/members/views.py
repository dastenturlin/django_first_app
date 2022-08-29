
# Create your views here.

# Django views are Python functions that takes http requests and
# returns http response, like HTML documents.

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world!")
