from django.urls import path

from .views import AddressView, SensorView, TemperatureView

urlpatterns = [
    path("", SensorView.as_view()),
    path("loc/", AddressView.as_view()),
    path("data/", TemperatureView.as_view()),
]
