from rest_framework import viewsets
from .models import Flight
from .serializers import FlightSerializer
from .filters import FlightFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from airline_management.reservations.models import Reservation
from airline_management.reservations.serializers import ReservationSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = FlightFilter

    @action(detail=True, methods=['get'])
    def reservations(self, request, pk=None):
        flight = self.get_object() 
        reservations = flight.reservations.all() 
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)