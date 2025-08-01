from rest_framework import viewsets
from .models import Reservation
from .serializers import ReservationSerializer
from .mail_service import send_reservation_confirmation_email

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        # Get passenger email from request data
        passenger_email = request.data.get("passenger_email")
        if passenger_email:
            send_reservation_confirmation_email(passenger_email)
        
        return response
