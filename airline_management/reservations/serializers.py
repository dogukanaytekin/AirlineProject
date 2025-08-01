from rest_framework import serializers
from airline_management.reservations.models import Reservation
from airline_management.flights.models import Flight

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def validate(self, data):
        flight = data.get('flight')
        if not flight:
            # Flight zorunlu, yoksa zaten başka hata verir ama garanti olsun
            raise serializers.ValidationError("Flight must be specified.")

        airplane = flight.airplane
        capacity = airplane.capacity

        # Aynı flight için mevcut rezervasyon sayısını al
        current_reservations = Reservation.objects.filter(flight=flight, status=True).count()

        if current_reservations >= capacity:
            raise serializers.ValidationError({
                'capacity_error': "This flight is fully booked. No more reservations allowed."
            })

        return data
