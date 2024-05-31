from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
            messages.info(request, ("Retry login"))
            return redirect('ogin.html')
    else:
        return render(request, 'authentication/login.html', {})