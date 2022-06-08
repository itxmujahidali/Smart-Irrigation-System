from django.contrib import admin
from .models import WebUser
from .models import Plant
from .models import Sensor
from .models import ScheduleWater

# Register your models here.
admin.site.register(WebUser)
admin.site.register(Plant)
admin.site.register(Sensor)
admin.site.register(ScheduleWater)
