
from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('statics', views.statics, name='statics'),
    path('addsensors', views.addsensors, name='addsensors'),
    path('login', views.login, name='login'),
    path('forgetpassword1', views.forgetpassword1, name='forgetpassword1'),
    path('forgetpassword2', views.forgetpassword2, name='forgetpassword2'),
    path('forgetpassword3', views.forgetpassword3, name='forgetpassword3'),
    path('forgetpassword4', views.forgetpassword4, name='forgetpassword4'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('settings', views.settings, name='settings'),
    # path('weather', weatherAPI.weather, name='weather'),
    path('error404', views.error404, name='error404'),
    path('error500', views.error500, name='error500'),
    path('sensor', views.sensor, name='sensor'),
] 