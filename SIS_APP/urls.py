from SIS_APP import weatherAPI
from django.contrib import admin
from django.urls import path

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    path('settings', views.settings, name='settings'),
    path('weather', weatherAPI.weather, name='weather'),
    path('error404', views.error404, name='error404'),
    path('error500', views.error500, name='error500'),
    path('sensor', views.sensor, name='sensor'),
] 