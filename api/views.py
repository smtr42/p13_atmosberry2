from rest_framework.utils import serializer_helpers
from api.models import Sensor
from rest_framework import generics, permissions
from .models import Sensor, Device, Address
from .serializers import SensorSerializer, AddressSerializer, TemperatureSerializer
from rest_framework.response import Response
from .permissions import IsAuthor0rReaOnly
from datetime import datetime, timedelta


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
            sensor_type=reading_data["sensor_type"]
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
        thetime = datetime.now() - timedelta(hours=48)
        device = Device.objects.filter(user=self.request.user)
        return Sensor.objects.filter(device=device[0])

        # return Sensor.objects.filter(device=device[0], timestamp__gte=thetime)