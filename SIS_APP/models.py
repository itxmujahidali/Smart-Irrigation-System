from django.db import models
from datetime import datetime
# Create your models here.
class WebUser(models.Model):

    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    farm_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    Password = models.CharField(max_length=50)
    account_created = datetime.now()

    def __str__(self):
        return self.name


class Plant(models.Model):

    plant_id = models.AutoField(primary_key=True)
    FK_plant = models.ForeignKey('WebUser', on_delete=models.CASCADE)
    plant_name = models.CharField(max_length=50) #card2
    number_of_plants = models.IntegerField() #card1
    number_of_sensors = models.IntegerField() #card3
    planted_area = models.IntegerField() #card4

    def __str__(self):
        return self.plant_name


class Sensor(models.Model):

    sensor_id = models.AutoField(primary_key=True)
    sensorID = str(sensor_id)
    FK_sensor = models.ForeignKey('Plant', on_delete=models.CASCADE)
    sensor_name = models.CharField(max_length=50)
    moistuer_level = models.IntegerField()
    sensor_update_time = models.DateTimeField( default=datetime.now)
    sensor_status = models.BooleanField(default=False)

    def __str__(self):
        return self.sensor_name

class WeatherAPI(models.Model):

    FK_weather = models.ForeignKey('WebUser', on_delete=models.CASCADE)

    city = models.CharField(max_length=100)
    city_id = models.IntegerField()
    temperature = models.FloatField()
    feels_like = models.FloatField()
    humidity = models.IntegerField()
    weather_report = models.CharField(max_length=30)
    wind_speed = models.FloatField()
    time_zone = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class ScheduleWater(models.Model):

    FK_schedule = models.ForeignKey('WebUser', on_delete=models.CASCADE)
    water_resource = models.CharField(max_length=50)
    water_flow = models.IntegerField()
    #knowledge base data here

    def __str__(self):
        return self.water_resource