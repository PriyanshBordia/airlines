from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, name="arrivals")
    duration = models.Integer()


class Passenger(models.Model):
    first = models.CharField(max_length=21)
    last = models.CharField(max_length=21)
    flights = models.ManyToMany()
