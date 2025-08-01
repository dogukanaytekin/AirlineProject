from django.db import models
from airline_management.flights.models import Flight  # ForeignKey için
import uuid
import string
import random
from django.utils import timezone

def generate_reservation_code():
    length = 6
    chars = string.ascii_uppercase + string.digits
    while True:
        code = ''.join(random.choices(chars, k=length))
        if not Reservation.objects.filter(reservation_code=code).exists():
            return code

class Reservation(models.Model):
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    reservation_code = models.CharField(max_length=10, unique=True, default=generate_reservation_code)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name='reservations')
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Reservation {self.reservation_code} for {self.passenger_name}"
