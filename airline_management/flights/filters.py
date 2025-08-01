from django_filters import rest_framework as filters
from airline_management.flights.models import Flight

class FlightFilter(filters.FilterSet):
    departure_time = filters.DateFilter(field_name="departure_time", lookup_expr='date')
    arrival_time = filters.DateFilter(field_name="arrival_time", lookup_expr='date')

    class Meta:
        model = Flight
        fields = ['departure', 'destination', 'departure_time', 'arrival_time']
