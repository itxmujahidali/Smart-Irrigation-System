
from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('statistics', views.statistics, name='statistics'),
    path('statistics/graph/<sensorid>', views.graph, name='graph'),
    path('addsensors', views.addsensors, name='addsensors'),
    path('login', views.login, name='login'),
    path('forgetpassword1', views.forgetpassword1, name='forgetpassword1'),
    path('forgetpassword1/forgetpassword2', views.forgetpassword2, name='forgetpassword2'),
    path('forgetpassword1/forgetpassword2/forgetpassword3', views.forgetpassword3, name='forgetpassword3'),
    path('forgetpassword1/forgetpassword2/forgetpassword3/forgetpassword4', views.forgetpassword4, name='forgetpassword4'),
    path('changepassword', views.changepassword, name='changepassword'),
    path('signout', views.signout, name='signout'),
    path('register', views.register, name='register'),
    path('settings', views.settings, name='settings'),
    path('dangerzone', views.dangerzone, name='dangerzone'),
    # path('weather', weatherAPI.weather, name='weather'),
    path('error404', views.error404, name='error404'),
    path('error500', views.error500, name='error500'),
    path('sensor/<link>', views.sensor, name='sensor'),
    path('pump', views.pump, name='pump'),
    path('pumpstatus/<str:link>', views.pumpstatus, name='pumpstatus'),
    # path("URL endpoint/"<path converter: URL link>, view_name.pumpstatus, name = "pumpstatus"),
    path('pumpoff', views.pump_off, name='pump_off'),
    path('doc', views.doc, name='doc'),
    # path('pump_automatic', views.pump_automatic, name='pump_automatic'),
] 