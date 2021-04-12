from django.shortcuts import render
from api.models import Device, Sensor
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from rest_framework.authtoken.models import Token
import binascii
import os
import django.utils.timezone as tz

def frontpage(request):
    return render(request, "pages/index.html")


@login_required
def dashboard(request):
    user = request.user
    devices = Device.objects.filter(user=user)
    sensors = Sensor.objects.filter(device__user=user)
    
    # a = CustomUser.objects.values(user=user)
    toke = Token.objects.filter(user=user)
    # toke = Token.objects.values().filter(user=user)

    print("Token : ", toke)
    return render(request, "pages/dashboard.html", {"devices": devices, "sensors": sensors, "token": toke})


@login_required
def refresh_token(request):
    key = binascii.hexlify(os.urandom(20)).decode()
    Token.objects.filter(user=request.user).update(key=key)
    print(f"changed the token as {key}")
    return dashboard(request)


@login_required
def add_device(request):
    pass


@login_required
def add_sensor(request):
    pass
