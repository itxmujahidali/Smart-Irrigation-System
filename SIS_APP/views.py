from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import WebUser

# Create your views here.

def index(request):
    return render(request, 'index.html')

# ------------------------------------------->  Login logic
def login(request):

    if (request.method == 'POST'):
        login_email = request.POST['email']
        login_password = request.POST['password']

        # Compare with Database where input email exist!
        try:
            CheckUser = WebUser.objects.get(email=login_email)
        except:
            return HttpResponse("User Dosen't Exist!")

        if (login_email == CheckUser.email and login_password == CheckUser.Password):
            return render(request, 'index.html')
        else:
            return HttpResponse("Email or Password are wrong!")

    else:
        return render(request, 'login.html')

# --------------------------------------------> END Login logic

############################################################################################

# ------------------------------------>  signup logic
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if(password1 == password2):
            password = password1
            # Sending HTML-Data to Model for store into Database!
            # Creating class object
            User = WebUser(name=name, email=email, Password=password)
            User.save()
            return render(request, 'login.html')
        else:
            return HttpResponse("Password didn't match!")

    else:
        return render(request, 'register.html')

# ----------------------------------> END signup logic


def error404(request):
    return render(request, 'error404.html')


def error500(request):
    return render(request, 'error500.html')


def settings(request):
    return render(request, 'account_settings.html')
