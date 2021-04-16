from django.urls import path

from .views import dashboard, frontpage, refresh_token, add_device, add_sensor

urlpatterns = [
    path("", frontpage, name="frontpage"),
    path("dashboard", dashboard, name="dashboard"),
    path("refresh", refresh_token, name="refresh"),
    path("add_device", add_device, name="add_device"),
    path("add_sensor", add_sensor, name="add_sensor"),
]

