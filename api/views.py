from datetime import timedelta

from django.utils import timezone
from rest_framework import generics
from rest_framework.response import Response

from .models import Address, Device, Sensor
from .permissions import IsAuthor0rReaOnly
from .serializers import (
    AddressSerializer,
    SensorSerializer,
    TemperatureSerializer,
)


class SensorView(generics.ListCreateAPIView):
    serializer_class = SensorSerializer
    permission_classes = (IsAuthor0rReaOnly,)

    def get_queryset(self):
        return Sensor.objects.all()

    def create(self, request, *args, **kwargs):
        reading_data = request.data
        new_reading = Sensor.objects.create(
            device=Device.objects.get(name=reading_data["device"]),
            name=reading_data["name"],
            timestamp=reading_data["timestamp"],
            measure=reading_data["measure"],
            sensor_type=reading_data["sensor_type"],
        )
        new_reading.save()
        serializer = SensorSerializer(new_reading)
        return Response(serializer.data)


class AddressView(generics.ListCreateAPIView):
    serializer_class = AddressSerializer
    permission_classes = (IsAuthor0rReaOnly,)

    def get_queryset(self):
        return Address.objects.all()


class TemperatureView(generics.ListCreateAPIView):
    serializer_class = TemperatureSerializer
    permission_classes = (IsAuthor0rReaOnly,)

    def get_queryset(self):
        device = Device.objects.filter(user=self.request.user)
        aware = timezone.now() - timedelta(hours=24)
        return Sensor.objects.filter(device=device[0], timestamp__gte=aware)
