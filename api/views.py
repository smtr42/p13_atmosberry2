from rest_framework.utils import serializer_helpers
from api.models import Sensor
from rest_framework import generics, permissions
from .models import Sensor, Device
from .serializers import SensorSerializer
from rest_framework.response import Response
from .permissions import IsAuthor0rReaOnly


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
