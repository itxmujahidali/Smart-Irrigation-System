import json, csv, os.path
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import WebUser
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    if request.session.has_key('id'):
        id = request.session.get('id')
        user = WebUser.objects.get(user_id=id)
        # return HttpResponse(name)
        return render(request, 'index.html',{'name':user.name})
    else:
        return render(request, 'login.html')

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
            #set session
            request.session['id'] = CheckUser.user_id
            return redirect(index)
            # request.session.set_expiry(300)
            # return render (request, 'index.html')
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



def settings(request):
    id = request.session.get('id')
    user =  WebUser.objects.get(user_id=id)
    user_name = user.name
    farm_name = user.farm_name
    user_email = user.email
    user_contact = user.contact
    if(request.method == "POST"):
        farm_name = request.POST['farmName']
        user_name = request.POST['name']
        user_email = request.POST['email']
        user_contact = request.POST['contact']
        User = WebUser(farm_name=farm_name, user_name=user_name, email=user_email, user_contact=user_contact)
        User.save()
        return render(request, 'account_settings.html',
            {"user_name":user_name,'user_email':user_email,"farm_name":farm_name,"user_contact":user_contact})
    else:
        return render(request, 'account_settings.html',
            {"user_name":user_name,'user_email':user_email,"farm_name":farm_name,"user_contact":user_contact})


def logout(request):
    request.session.flush()
    return render(request, 'login.html')

@csrf_exempt
def sensor(request):

    from datetime import datetime

    # Only listen to PUT requests
    # if request.method != "PUT" or request.body == None:
    #     response_message = "Only PUT requests are allowed on this route."
    #     response_code = 405
    #     return HttpResponse(response_message,response_code)
    # else:
    
    # Load body
    body = json.loads(request.body)

    # datetime object containing current date and time
    now = datetime.now()

    print (body["sensor_name"])
    sensor_name = (body["sensor_name"])

    print (body["reading"])
    reading = (body["reading"])

    # print (body["positionX"])
    # positionX = (body["positionX"])

    # print (body["current_moisture"])
    # current_moisture = (body["current_moisture"])

    # datetime object containing current date and time
    now = datetime.now()
    date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    print("date and time =", date, time)

    if (os.path.isfile("data.csv")):  
        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([sensor_name, reading," ", date, time])
            writer.writerow([sensor_name, reading," ", date, time])
    else:
         with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([sensor_name, reading," ", date, time])

    return HttpResponse ("Success!")

    # if 'email' not in body or 'positionX' not in body or 'positionY' not in body\
    #                         or 'password' not in body or 'current_moisture' not in body:
    #     response_message = "Missing required plant or grid information."
    #     response_code = 400
    #     return HttpResponse(response_message)

    # email = body['email']
    # password = body['password']
    # positionX = body['positionX']
    # positionY = body['positionY']
    # current_moisture = body['current_moisture']
    # return HttpResponse(email)


def error404(request, exception):
    context = {}
    return render(request, 'error404.html',context)


def error500(request,*args, **kwargs):
    context = {}
    return render(request, 'error500.html',context)