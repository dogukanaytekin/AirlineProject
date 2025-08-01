from rest_framework import viewsets
from .models import Airplane
from .serializers import AirplaneSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from airline_management.flights.serializers import FlightSerializer

class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    @action(detail=True, methods=['get'])
    def flights(self, request, pk=None):
        airplane = self.get_object()
        flights = airplane.flights.all()  
        serializer = FlightSerializer(flights, many=True)
        return Response(serializer.data)



