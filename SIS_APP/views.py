import json, csv, os.path, requests
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import WebUser, WeatherAPI
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def index(request):
    if request.session.has_key('id'):
        id = request.session.get('id')
        user = WebUser.objects.get(user_id=id)

        
    try:
        id = request.session['id'] #getting id by session
        info = WeatherAPI.objects.filter(FK_weather = id)
        CITY = info[0].city
    except:
        return HttpResponse ("City Error!")


    # Your API key
    API_KEY = "84b2833cfdc8bca61f826270f0c4dc55"

    # updating the URL
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"

    # Sending HTTP request
    response = requests.get(URL)

    # checking the status code of the request
    if response.status_code == 200:
        
        # retrieving data in the json format
        data = response.json()
        
        # take the main dict block
        main = data['main']
        
        # getting temperature
        temperature = main['temp']
        temperature_celsius = temperature - 273.15
        # getting feel like
        temp_feel_like = main['feels_like']
        temp_feel_like_celsius = temp_feel_like - 273.15
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        # pressure = main['pressure']
        
        # weather report
        weather_report = data['weather']
        # wind report
        wind_report = data['wind']
        
        CITY = CITY.upper() #All Uppercase Letter of City

        dic_tempreature =  int(temperature_celsius)
        dic_feels_like =  int(temp_feel_like_celsius)
        dic_humidity =  humidity
        dic_description =  weather_report[0]['description']
        dic_description = dic_description.capitalize() #Capitalize First Letter
        dic_speed =  wind_report['speed']
        dic_timezone =  data['timezone']

        #Save value in database
        # webuser = WebUser.objects.get(user_id=5)
        # api_database = WeatherAPI(FK_weather=webuser,city=CITY, city_id=dic_id, temperature=dic_tempreature, feels_like=dic_feels_like, 
        # humidity=dic_humidity, weather_report=dic_description, wind_speed=dic_speed, time_zone=dic_timezone)
        # api_database.save()

        return render (request, 'index.html', {
            'name': user.name,
            'CITY': CITY,
            'dic_tempreature': dic_tempreature,
            'dic_feels_like': dic_feels_like,
            'dic_humidity': dic_humidity,
            'dic_description': dic_description,
            'dic_speed': dic_speed,
            'dic_timezone': dic_timezone,}
            )

    else:
        # showing the error message
        return HttpResponse ("Error in the HTTP request")


    ##################################################################################################

    # API Credentials
    # wesite: www.openweathermap.com
    # username: fypmujahidali
    # password: openweathermap00
    # email: thisalitalks@gmail.com




        # return HttpResponse(name)
    #     return render(request, 'index.html',{'name':user.name})
    # else:
    #     return render(request, 'login.html')

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