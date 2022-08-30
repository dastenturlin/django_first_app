
# Create your views here.

# Django views are Python functions that takes http requests and
# returns http response, like HTML documents.

from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Members

# R = READ
def index(request):
    mymembers = Members.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'mymembers': mymembers,
    }
    # output = ""
    # for x in mymembers:
    #     output = output + " " + x["firstname"]
    # template = loader.get_template('myfirst.html')
    # return HttpResponse(output)
    return HttpResponse(template.render(context, request))

# just a method for generating a webpage to add record
def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

# C = CREATE, the actual adding the record
def addrecord(request):
    firstname = request.POST['first']
    lastname = request.POST['last']
    member = Members(firstname=firstname, lastname=lastname)
    member.save()

    return HttpResponseRedirect(reverse('index'))

# D = DELETE
def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()

    return HttpResponseRedirect(reverse('index'))

# just a webpage to update the record
def update(request, id):
    mymember = Members.object.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember': mymember,
    }
    return HttpResponse(template.render(context, request))

# the actual U = UPDATE
def updaterecord(request):
    first = request.POST['first']
    last = request.POST['last']
    member = Members.objects.get(id=id)
    member.firstname = first
    member.lastname = last
    member.save()
    return HttpResponseRedirect(reverse('index'))

