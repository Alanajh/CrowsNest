from django.http import HttpResponse
from django.template import loader

def logins(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())