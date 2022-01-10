from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Guest ,Reservation,Movie
#1 without REST and no modelquery
def no_rest_no_model(request):

    guests=[
        {
            'id':1,
            'name':'ehab',
            'mobile':123456789,
            
        },
        {
            'id':2,
            'name':'mohamed',
            'mobile':123456789,

        }
    ]
    return JsonResponse (guests,safe=False)


#2 no rest and from model 
def no_rest_from_model(request):
    data = Guest.objects.all()
    response = {
        'guests':list(data.values('name','mobile'))
    }
    return JsonResponse(response)