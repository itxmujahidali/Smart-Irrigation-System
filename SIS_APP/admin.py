from django.contrib import admin

from SIS_APP.views import sensor
from .models import WebUser
from .models import Plant
from .models import Sensor
from .models import ScheduleWater

# Register your models here.

#This lines show simple view in admin pannel
admin.site.register(Plant)
admin.site.register(ScheduleWater)

#This lines show Advance view in admin pannel
@admin.register(WebUser)
class WebUserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "name", "email", "city")

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ("FK_sensor", "sensor_name", "sensorkey", "moistuer_level", "sensor_update_time")