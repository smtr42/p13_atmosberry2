from django.contrib import admin

from .models import Address, Device, Sensor

admin.site.register(Sensor)
admin.site.register(Address)
admin.site.register(Device)
