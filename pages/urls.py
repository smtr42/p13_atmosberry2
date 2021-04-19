from django.urls import path

from .views import (
    about,
    add_device,
    add_sensor,
    dashboard,
    frontpage,
    refresh_token,
)

urlpatterns = [
    path("", frontpage, name="frontpage"),
    path("dashboard", dashboard, name="dashboard"),
    path("about", about, name="about"),
    path("refresh", refresh_token, name="refresh"),
    path("add_device", add_device, name="add_device"),
    path("add_sensor", add_sensor, name="add_sensor"),
]
