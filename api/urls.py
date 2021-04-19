from django.urls import path

from .views import AddressView, SensorView, TemperatureView

urlpatterns = [
    path("", SensorView.as_view(), name="api_index"),
    path("loc/", AddressView.as_view(), name="loc"),
    path("data/", TemperatureView.as_view(), name="data"),
]
