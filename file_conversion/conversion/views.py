from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from .models import User
from .forms import UserForm, InputForm
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
    if request.method == "POST":
        searched = request.POST['searched']
    
    return render(request, 'search_users.html', {'searched':searched})

def accounts_list(request):
    acct_list = User.objects.all()
    return render(request,  'all_accounts.html', {'acct_list': acct_list})

def create_account(request):
    submitted = False
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/create_account?submitted=True')
    else:
        form = UserForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'create_account.html', {'form': UserForm, 'submitted': submitted})
        #  return render(request, 'create_account.html', {'form': UserForm, 'submitted': submitted})

def search_users(request):
    if request.method == "POST":
        user = request.POST['user']
        pswd = request.POST['pswd']
        # Returned results for username and password
        account_name = User.objects.filter(username__contains=user)
        account_pswd = User.objects.filter(password__contains=pswd)

        return render(request, 'search_users.html', {"user":user, "pswd": pswd, 
            'account_name': account_name, 'account_pswd': account_pswd})
    
def main(request):
    return render(request, 'main.html', {'form': InputForm})