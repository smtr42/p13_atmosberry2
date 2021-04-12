"""
Serializers transform data into Json andscpecify wich
fields to include or exclude.
"""

from rest_framework import serializers
from .models import Device, Sensor, Address


class SensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ('name', 'timestamp', 'measure', 'sensor_type')

    # def create(self, validated_data):
    #     readings_data = validated_data.pop('measure')

    #     sensor = Sensor.objects.create(**validated_data)

    #     for readings in readings_data:
    #         Reading.objects.create(sensor=sensor, **readings)
    #     return sensor


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('lat', 'lon', 'user')


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('name', 'timestamp', 'measure', 'sensor_type', 'device')