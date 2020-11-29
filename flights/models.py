from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=6)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city}: ({self.code})"

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name = "departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name = "arrivals")
    duration =models.IntegerField()

    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"
    
    def is_valid_flight(self):
        return self.origin != self.destination and self.duration > 0

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    # passengers have a many to many relationship with flights
    # blank is True as there can be passengers with no flights
    flights = models.ManyToManyField(
        Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"





