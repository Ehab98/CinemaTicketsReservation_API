
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
    #3 GET POST from rest framework function based view @api_view
    path('3/',views.FBV_List),
    #4 GET PUT DELETE from rest framework function based view @api_view
    path('4/<int:pk>',views.FBV_pk),
    
    #5 GET POST from rest framework Class based view APIVIEW
    path('5/',views.CBV_List.as_view()),

    #6 GET PUT DELETE from rest framework Class based view APIVIEW
    path('6/<int:pk>',views.CBV_pk.as_view()),
    ####################
    path('api-auth/', include('rest_framework.urls'))
]
