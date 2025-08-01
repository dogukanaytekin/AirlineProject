from django.db import models
from airline_management.airplanes.models import Airplane  

class Flight(models.Model):
    flight_number = models.CharField(max_length=20)
    departure = models.CharField(max_length=100)  
    destination = models.CharField(max_length=100)  
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name='flights')

    def __str__(self):
        return f"{self.flight_number}: {self.departure} -> {self.destination}"
