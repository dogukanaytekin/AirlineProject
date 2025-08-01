from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AirplaneViewSet

router = DefaultRouter()
router.register(r'airplanes', AirplaneViewSet, basename='airplane')

urlpatterns = [
    path('', include(router.urls)),
]

