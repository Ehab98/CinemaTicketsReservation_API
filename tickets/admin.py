from django.contrib import admin
from .models import Guest,Movie,Reservation

#Guest Register
admin.site.register(Guest)

#Movie Register
admin.site.register(Movie)

#Reservation Register
class reservation(admin.ModelAdmin):
    list_display = ('guest','movie')
admin.site.register(Reservation,reservation)

