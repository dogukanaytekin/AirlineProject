from rest_framework import serializers
from django.utils.timezone import timedelta
from airline_management.flights.models import Flight

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

    def validate(self, data):
        airplane = data.get('airplane')
        departure_time = data.get('departure_time')
        arrival_time = data.get('arrival_time')

        # Güncelleme sırasında eski instance verisi varsa, ekik alanları tamamla
        if self.instance:
            airplane = data.get('airplane', self.instance.airplane)
            departure_time = data.get('departure_time', self.instance.departure_time)
            arrival_time = data.get('arrival_time', self.instance.arrival_time)

        # Aynı uçağın diğer uçuşlarını getir (güncelleniyorsa kendisi hariç tut)
        existing_flights = Flight.objects.filter(airplane=airplane)
        if self.instance:
            existing_flights = existing_flights.exclude(pk=self.instance.pk)

        one_hour = timedelta(hours=1)

        for flight in existing_flights:
            # Yeni uçuş kalkış zamanı, mevcut uçuşun varış zamanına çok yakın mı?
            if abs((departure_time - flight.arrival_time)) < one_hour:
                raise serializers.ValidationError({
                'flight_time_error': "There must be at least 1-hour difference between two flights of the same aircraft."
                })

            # Yeni uçuş varış zamanı, mevcut uçuşun kalkış zamanına çok yakın mı?
            if abs((arrival_time - flight.departure_time)) < one_hour:
                raise serializers.ValidationError({
                'flight_time_error': "There must be at least 1-hour difference between two flights of the same aircraft."
                })


        return data
