from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('airline_management.airplanes.urls')),
    path('api/', include('airline_management.flights.urls')),
    path('api/', include('airline_management.reservations.urls')),
]
