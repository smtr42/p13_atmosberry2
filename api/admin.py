from django.contrib import admin
from .models import Sensor, Device, Address


admin.site.register(Sensor)
admin.site.register(Address)
admin.site.register(Device)