from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import User

def logins(request):
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render())
    accounts = User.objects.all()
    accts = User.objects.filter(username="test").values()
    template = loader.get_template('index.html')
    context = {
        'userAccounts': accts,
    }
    return HttpResponse(template.render(context, request))

def valid_user(request):
    
    return render(request, 'conversion/index.html', {})