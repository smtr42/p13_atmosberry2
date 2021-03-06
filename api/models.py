from django.conf import settings
from django.db import models

# https://www.django-rest-framework.org/api-guide/authentication/


class Device(models.Model):
    """The Device, such as Raspberry zero"""

    name = models.CharField(max_length=50, unique=True)
    # CONSTRAINT
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="device_user",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Address(models.Model):
    """Adresse related to the Device"""

    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    # CONSTRAINT
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="address_user",
        on_delete=models.CASCADE,
    )
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.city


class Sensor(models.Model):
    """The sensor and its measurement"""

    TEMPERATURE = "T"
    HUMIDITY = "Hu"
    PRESSURE = "P"
    SENSOR_TYPE_CHOICE = [
        (TEMPERATURE, "Temperature"),
        (HUMIDITY, "Humidity"),
        (PRESSURE, "Pressure"),
    ]

    name = models.CharField(max_length=150)
    timestamp = models.DateTimeField()
    measure = models.FloatField(blank=True, null=True)
    sensor_type = models.CharField(
        max_length=2,
        choices=SENSOR_TYPE_CHOICE,
        default=TEMPERATURE,
    )
    # CONSTRAINT
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
