
# Create your views here.

# Django views are Python functions that takes http requests and
# returns http response, like HTML documents.

from django.http import HttpResponse
from django.template import loader
from .models import Members

def index(request):
    mymembers = Members.objects.all().values()
    output = ""
    for x in mymembers:
        output = output + " " + x["firstname"]
    template = loader.get_template('myfirst.html')
    return HttpResponse(output)
