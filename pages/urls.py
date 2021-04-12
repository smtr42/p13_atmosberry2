from django.urls import path

from .views import dashboard, frontpage, refresh_token

urlpatterns = [
    path("", frontpage, name="frontpage"),
    path("dashboard", dashboard, name="dashboard"),
    path("refresh", refresh_token, name="refresh"),
]
