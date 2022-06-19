from asyncio.windows_events import NULL
from django.db import models
from datetime import datetime
# Create your models here.
class WebUser(models.Model):

    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    farm_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50)
    contact = models.CharField(max_length=50, null=True)
    Password = models.CharField(max_length=50)
    recovery_code = models.CharField(max_length=6, null=True)
    city = models.CharField(max_length=100)
    pump = models.IntegerField(null=True)
    account_created = datetime.now()

    def __str__(self):
        return self.name

class Sensor(models.Model):

    sensor_id = models.AutoField(primary_key=True)
    sensorkey = models.IntegerField(null=True)
    FK_sensor = models.ForeignKey('WebUser', on_delete=models.CASCADE)
    sensor_name = models.CharField(max_length=50, null=True)
    plant_name = models.CharField(max_length=50, null=True)
    moistuer_level = models.IntegerField( blank=True, null=True)
    sensor_update_time = models.DateTimeField( default=datetime.now,  blank=True, null=True)

    def __str__(self):
        return self.sensor_name
