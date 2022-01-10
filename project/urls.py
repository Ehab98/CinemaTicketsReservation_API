
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #1
    path('1/',views.no_rest_no_model),
    #2
    path('2/',views.no_rest_from_model),
    #3
    path('3/',views.no_rest_from_model),
    ####################
    path('api-auth/', include('rest_framework.urls'))
]
