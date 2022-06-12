from asyncio.windows_events import NULL
import json, csv, os.path, requests
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import WebUser, Sensor
from django.views.decorators.csrf import csrf_exempt
import smtplib
from random import randint


# Create your views here.

def index(request):
    try:
        if request.session.has_key('id'):
            id = request.session.get('id')
            user = WebUser.objects.get(user_id=id)

            
        try:
            id = request.session['id'] #getting id by session
            info = WebUser.objects.filter(user_id = id)
            CITY = info[0].city
        except:
            return render (request, "login.html")


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
    except:
            return render (request, "index.html")
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
        city = request.POST['city']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if(password1 == password2):
            password = password1
            # Sending HTML-Data to Model for store into Database!
            # Creating class object
            User = WebUser(name=name, email=email, city=city, Password=password)
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
    user_lname = user.lname
    user_city = user.city
    farm_name = user.farm_name
    contact = user.contact
    if(request.method == "POST"):
        input_farm_name = request.POST['farmName']
        input_name = request.POST['name']
        input_lname = request.POST['lname']
        input_cityname = request.POST['cityname']
        input_contact = request.POST['contact']
        #User = WebUser(farm_name=input_farm_name, name=input_name, contact=input_contact)
        user.name = input_name
        user.lname = input_lname
        if (input_cityname == ""):
            pass
        else:
            user.city = input_cityname
        user.farm_name = input_farm_name
        user.contact = input_contact
        user.save(update_fields=['name','lname', 'city', 'farm_name','contact'])
        return render(request, 'account_settings.html',
            {"user_name":user_name,"farm_name":farm_name,"contact":contact, "user_city":user_city })
    else:
        #return HttpResponse (user_name)
        return render(request, 'account_settings.html',
            {"user_name":user_name,"user_lname":user_lname,"farm_name":farm_name,"contact":contact})


def graph(request, sensorid):
    sensor_id = int(sensorid)
    sensor = Sensor.objects.filter(sensorkey=sensorid)
    moisture_level_list = []
    sensor_update_time_list = []

    for sensor_index in sensor:
        moisture_level = sensor_index.moistuer_level
        sensor_update_time = sensor_index.sensor_update_time
        moisture_level_list.append(moisture_level)
        sensor_update_time_list.append(sensor_update_time)
    slice_moisture_level_list = moisture_level_list[-1:-11:-1]
    slice_moisture_level_list = slice_moisture_level_list[-1:-11:-1]
    # print(f'{"moisture_level_list---------------->",slice_moisture_level_list}')
    slice_sensor_update_time_list = sensor_update_time_list[-1:-11:-1]
    slice_sensor_update_time_list = slice_sensor_update_time_list[-1:-11:-1]

    return render(request, 'graph.html', context={
        "sensor_id": sensor_id, "moisture_level_list": slice_moisture_level_list, "sensor_update_time_list": slice_sensor_update_time_list
    })

def statistics(request):
    id = request.session.get('id')
    sensor = Sensor.objects.filter(FK_sensor=id)
    # sensor = Sensor.objects.filter(FK_sensor=id, sensorkey=112233).order_by('-sensorkey')[:5]
    try:
        sensor_key_list = []
        # sensor_name_list = []
        sensor_name_list = []
        sensor_plant_list = []
        # sensor_update_time_list = []

        for sensor_index in sensor:
            sensor_key = sensor_index.sensorkey
            # sensor_name = sensor_index.sensor_name
            sensor_name = sensor_index.sensor_name
            sensor_plant = sensor_index.plant_name
            # sensor_update_time = sensor_index.sensor_update_time

            sensor_key_list.append(sensor_key)
            # sensor_name_list.append(sensor_name)
            sensor_name_list.append(sensor_name)
            sensor_plant_list.append(sensor_plant)
            # sensor_update_time_list.append(sensor_update_time)

        temp_sensor_name = sensor_name_list[-1]
        temp_plant_name = sensor_plant_list[-1]
        # temp_sensor_update_time = sensor_update_time_list[-1]

        # print(f'{"temp_moisture_level----->",temp_sensor_name}')
        #Generating unique sensor key

        unique_sensor_key = []
        # insert the list to the set
        list_set = set(sensor_key_list)
        # convert the set to the list
        unique_sensor_key = (list(list_set))

        return render(request, 'statistics.html', context={
            "unique_sensor_key": unique_sensor_key, "temp_sensor_name": temp_sensor_name, "temp_plant_name" : temp_plant_name,
            
            })
    except:
        return HttpResponse("Please Add Some Sensors!")

def changepassword(request):
    id = request.session.get('id')
    user =  WebUser.objects.get(user_id=id)
    user_password = user.Password
    if(request.method == "POST"):
        current_password= request.POST['currentpassword']
        new_password = request.POST['newpassword']
        confirm_password = request.POST['confirmpassword']
        if (current_password == user_password):
            if (new_password == confirm_password):
                user.Password = new_password
                user.save(update_fields=['Password'])
                return render(request, 'changepassword.html')
            else:
                return HttpResponse ("Your New Password is not match with confirm password!")
        else:
            return HttpResponse("Your Current password is incorrect!")
    return render(request, 'changepassword.html')

def dangerzone(request):
    if (request.method == "POST"):
        id = request.session.get('id')
        user =  WebUser.objects.get(user_id=id)
        user.delete()
        return render(request, 'login.html')

    else:
        return render(request, 'deleteaccount.html')

def addsensors(request):
    if (request.method == "POST"):
        id = request.session.get('id')
        input_sensorid = request.POST['sensorid']
        input_sensor_name = request.POST['sensorname']
        input_plantname = request.POST['plantname']

        try:

            #must use objects.get when you add data in DB through foreign key
            id = request.session.get('id')
            user =  WebUser.objects.get(user_id=id)

            key = ""
            filter_sensor_key =  Sensor.objects.filter(sensorkey=input_sensorid)
            for loop in filter_sensor_key:
                key = loop.sensorkey
            
            # key = filter_sensor_key.sensorkey
            
            input_sensorid = int(input_sensorid)
            # print(type(input_sensorid))
            print(key)
            if(key != input_sensorid or key == ""):

                moisture = 0
                #add data through foreign key in database
                sensor = Sensor.objects.create(FK_sensor=user, sensorkey=input_sensorid, plant_name=input_plantname, sensor_name=input_sensor_name,
                    moistuer_level= moisture
                )
                sensor.save()
                # print(user_id)
                return render(request, 'addsensors.html')
            else:
                return HttpResponse("SensorID is already taken!")
        except:
            return HttpResponse("Something went wrong!")
    else:
        return render(request, 'addsensors.html')


def forgetpassword1(request):
    if(request.method == "POST"):
        email = request.POST['email']

        # Compare with Database where input email exist!
        try:
            CheckEmail = WebUser.objects.get(email=email)
        except:
            return HttpResponse("Please enter your correct email!")
        
        if (email == CheckEmail.email):
            #send email code
            #try:
                gmail_user = "samswebdev58@gmail.com"
                gmail_pwd = "Skype123."
                TO = email
                SUBJECT = "SIS Recovery Code"
                TEXT = "Your recovery code is: "
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(gmail_user, gmail_pwd)

                #generating random numbers
                number_generate = randint(100001,999999)

                BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_user,
                        'Subject: %s' % SUBJECT,
                        '', TEXT+str(number_generate)])

                server.sendmail(gmail_user, [TO], BODY)

                CheckEmail = WebUser.objects.get(email=email)
                CheckEmail.recovery_code = number_generate
                CheckEmail.save()

                print (f'Email has been send! \nRecovery code is: {number_generate}')
                return render(request, 'forgetpassword2.html', {"email": email})
                
            #except:
                #return HttpResponse(email)
        else:
            return HttpResponse("Your Email isn't match with our database record!")
        #return render(request, 'forgetpassword2.html')
    
    else:
        return render(request, 'forgetpassword1.html')

def forgetpassword2(request):
    if (request.method == "POST"):
        user_email = request.POST["email"]
        print(user_email)

        try:
            six_digit_code = request.POST["six_digit_code"]
            print(six_digit_code)
            # Compare with Database where input email exist!
            print(f"Six Digit code is:{six_digit_code}")
            #print(six_digit_code)

            #---------------------------------ERRRRRRRRRRRRRRRRRRRRRROOOOOOOOOOOOOOOOOOORRRRRRRRRRRRRR__________________
            CheckEmail = WebUser.objects.get(email="thisalitalks@gmail.com")
            print(CheckEmail.recovery_code)
            code = CheckEmail.recovery_code
            print(f"code is:{code}")

            if (six_digit_code == code):
                return render(request, 'forgetpassword3.html', {"email":user_email})
                return HttpResponse("Code has been matched with database code. Test Successfull!")
            else:
                return HttpResponse("Code hasn't been matched!")

        except:
            #return HttpResponse("Running Exception code! ")
            return render(request, 'forgetpassword2.html')    
    else:
        return HttpResponse("ELSE CONDITION")

def forgetpassword3(request):
    return render(request, 'forgetpassword3.html')

def forgetpassword4(request):
    return render(request, 'forgetpassword4.html')

def logout(request):
    request.session.flush()
    return render(request, 'login.html')

@csrf_exempt
def sensor(request, link):

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

    # print (body["sensor_name"])
    user_id = (body["user_id"])
    user_id = int(user_id)
    sensor_key = (body["sensor_key"])
    sensor_name = (body["sensor_name"])
    plant_name = (body["plant_name"])
    moisture_level = (body["moisture_level"])

    #must use objects.get when you add data in DB through foreign key
    user =  WebUser.objects.get(user_id=user_id)
    # #add data through foreign key in database
    sensor = Sensor.objects.create(FK_sensor=user, sensorkey=sensor_key, plant_name=plant_name, sensor_name=sensor_name,
        moistuer_level= moisture_level
    )
    sensor.save()

    print(f'{"URL ---------------->",link}')
    print(f'{"USER ID ---------------->",user_id, type(user_id)}')
    print(f'{"sensor_name ---------------->",sensor_name}')
    print(f'{"sensor_key ---------------->",sensor_key}')
    print(f'{"plant_name ---------------->",plant_name}')
    print(f'{"moisture_level 1 ---------------->",moisture_level}')





    # sensor_name2 = (body["sensor_name2"])
    # print(f'{"Sensor 2 ---------------->",sensor_name2}')
    

    # print (body["reading"])
    # reading = (body["reading"])

    # print (body["positionX"])
    # positionX = (body["positionX"])

    # print (body["current_moisture"])
    # current_moisture = (body["current_moisture"])

    # datetime object containing current date and time
    # now = datetime.now()
    # date = now.strftime("%d/%m/%Y")
    # time = now.strftime("%H:%M:%S")
    # print("date and time =", date, time)

    if (os.path.isfile("data.csv")):  
        with open('data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            # writer.writerow([sensor_name, reading," ", date, time])
            # writer.writerow([sensor_name, reading," ", date, time])
    else:
         with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            # writer.writerow([sensor_name, reading," ", date, time])

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


def pump(request):
    talk = 1
    return HttpResponse (talk)

def error404(request, exception):
    context = {}
    return render(request, 'error404.html',context)


def error500(request,*args, **kwargs):
    context = {}
    return render(request, 'error500.html',context)