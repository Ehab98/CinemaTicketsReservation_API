from django.db import models
from django.db.models.fields import CharField


class Movie(models.Model):

    hall = models.CharField(max_length=50)
    movie = models.CharField(max_length=50)
    date = models.DateField()


    class Meta:
        verbose_name = ("Movie")
        verbose_name_plural = ("Movies")

    def __str__(self):
        return self.movie



class Guest(models.Model):

    
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    class Meta:
        verbose_name = ("Guest")
        verbose_name_plural = ("Guests")

    def __str__(self):
        return self.name


class Reservation(models.Model):

    
    guest = models.ForeignKey("Guest",related_name='reservation', on_delete=models.CASCADE)
    movie = models.ForeignKey("Movie",related_name='reservation', on_delete=models.CASCADE)
    class Meta:
        verbose_name = ("Reservation")
        verbose_name_plural = ("Reservations")

    def __str__(self):
        return self.movie

