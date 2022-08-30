
# Create your views here.

# Django views are Python functions that takes http requests and
# returns http response, like HTML documents.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

def homepage(request):
    return HttpResponse("Hello world!")