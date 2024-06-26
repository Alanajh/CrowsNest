from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def login_user(request):
    # Verify the form is filled out
    if request.method == "POST":
        user = request.POST['user']
        pswd = request.POST['pswd']
        user = authenticate(request, username=user, password=pswd)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            # Login was not valid message
            messages.success(request, ("Retry login"))
            return redirect('login')
    else:
        return render(request, 'authentication/login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, (" Logged out "))
    return redirect('login')

def create_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("User created"))
            return redirect('main')
    else:
        form = UserCreationForm()       
    return render(request, 'authentication/create_user.html', 
                    {'form':form})