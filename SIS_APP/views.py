from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'index.html')

def login(request):
    return render (request, 'login.html')

def register(request):
    return render (request, 'register.html')

def error404(request):
    return render (request, 'error404.html')

def error500(request):
    return render (request, 'error500.html')

def settings(request):
    return render (request, 'account_settings.html')