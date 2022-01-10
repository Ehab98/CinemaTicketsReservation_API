from django.contrib import admin
from .models import Guest,Movie,Reservation

#Guest Register
admin.site.register(Guest)

#Movie Register
admin.site.register(Movie)

#Reservation Register
admin.site.register(Reservation)

