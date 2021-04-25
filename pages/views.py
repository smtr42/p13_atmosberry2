import binascii
import logging
import os

from django.apps import apps
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from rest_framework.authtoken.models import Token

from api.models import Device, Sensor

from .forms import DeviceForm, SensorForm

logger = logging.getLogger(__name__)


def frontpage(request):
    return render(request, "pages/index.html")


def about(request):
    return render(request, "pages/about.html")


@login_required
def dashboard(request):
    logger.info("################# test")

    user = request.user
    devices = Device.objects.filter(user=user).values(
        "address__lat", "name", "address__lon"
    )
    sensors = Sensor.objects.filter(device__user=user)
    toke = Token.objects.filter(user=user)
    return render(
        request,
        "pages/dashboard.html",
        {
            "devices": devices,
            "sensors": sensors,
            "token": toke,
            "device_form": DeviceForm,
            "sensor_form": SensorForm(user),
        },
    )


@login_required
def refresh_token(request):
    if request.method != "POST":
        raise Http404("Bad request")
    key = binascii.hexlify(os.urandom(20)).decode()
    # obj, created = Token.objects.filter(user=request.user).update_or_create(key=key)
    print("#################", request.user)
    print(key)
    obj, created = Token.objects.update_or_create(user=request.user, key=key)
    return dashboard(request)


@login_required
def add_device(request):
    if request.method != "POST":
        raise Http404("Bad request")
    user = request.user
    form = DeviceForm(request.POST)
    device_model = apps.get_model("api", "Device")
    address_model = apps.get_model("api", "Address")
    if form.is_valid():
        device_name = form.cleaned_data.get("device")
        lat = form.cleaned_data.get("lat")
        lon = form.cleaned_data.get("lon")
        device_model.objects.create(user=user, name=device_name)
        device = device_model.objects.get(user=user, name=device_name)
        address_model.objects.create(
            user=user, lat=lat, lon=lon, device=device
        )
    return dashboard(request)


@login_required
def add_sensor(request):
    if request.method != "POST":
        raise Http404("Bad request")
    user = request.user
    form = SensorForm(user, request.POST)

    if form.is_valid():
        print(form.cleaned_data)
        print("form is valid")
    return dashboard(request)
