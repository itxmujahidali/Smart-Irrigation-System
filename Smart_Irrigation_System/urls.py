from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404, handler500, handler403, handler400
from SIS_APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SIS_APP.urls')),
]
handler404 = 'SIS_APP.views.error404'
# handler500 = 'SIS_APP.views.error500'
# handler403 = 'SIS_APP.views.error_403'
# handler400 = 'SIS_APP.views.error_400'
''' Checking Errors
    
    path('index/', include('SIS_APP.urls')),
    path('statics/', include('SIS_APP.urls')),
    path('addsensors/', include('SIS_APP.urls')),
    path('login/', include('SIS_APP.urls')),
    path('forgetpassword1/', include('SIS_APP.urls')),
    path('forgetpassword1/forgetpassword2/', include('SIS_APP.urls')),
    path('forgetpassword1/forgetpassword2/forgetpassword3/', include('SIS_APP.urls')),
    path('forgetpassword4/', include('SIS_APP.urls')),
    path('logout/', include('SIS_APP.urls')),
    path('register/', include('SIS_APP.urls')),
    path('settings/', include('SIS_APP.urls')),
    path('error404/', include('SIS_APP.urls')),
    path('error500/', include('SIS_APP.urls')),
    path('sensor/', include('SIS_APP.urls')), 
    '''

