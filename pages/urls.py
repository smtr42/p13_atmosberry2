from django.urls import path

from .views import dashboard, frontpage

urlpatterns = [
    path("", frontpage, name="frontpage"),
    path("dashboard", dashboard, name="dashboard"),
]
