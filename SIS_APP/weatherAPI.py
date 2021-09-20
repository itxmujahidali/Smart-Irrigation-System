# importing modules
from django.http.response import HttpResponse
from .models import WeatherAPI, WebUser
from django.shortcuts import render
import requests, json

def weather(request):

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

        dic_id = data['id']
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

        return render (request, 'weather.html', {
            'CITY': CITY,
            'dic_id': dic_id,
            'dic_tempreature': dic_tempreature,
            'dic_feels_like': dic_feels_like,
            'dic_humidity': dic_humidity,
            'dic_description': dic_description,
            'dic_speed': dic_speed,
            'dic_timezone': dic_timezone}
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

