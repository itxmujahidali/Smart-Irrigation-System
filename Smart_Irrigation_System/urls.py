from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SIS_APP.urls')),
    path('index', include('SIS_APP.urls')),
    path('login', include('SIS_APP.urls')),
    path('register', include('SIS_APP.urls')),
    path('settings', include('SIS_APP.urls')),
    path('weather', include('SIS_APP.urls')),
    path('error404', include('SIS_APP.urls')),
    path('error500', include('SIS_APP.urls')),
]
