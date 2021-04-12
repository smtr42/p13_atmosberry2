from django.urls import path
from .views import SensorView, AddressView, TemperatureView

urlpatterns = [
    path('', SensorView.as_view()),
    path('loc/', AddressView.as_view()),
    path('data/', TemperatureView.as_view()),
]
