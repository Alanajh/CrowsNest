from django.http import HttpResponse
from django.template import loader
from .models import User

def logins(request):
    #template = loader.get_template('index.html')
    #return HttpResponse(template.render())
    accounts = User.objects.all()
    template = loader.get_template('index.html')
    context = {
        'userAccounts': accounts,
    }
    return HttpResponse(template.render(context, request))