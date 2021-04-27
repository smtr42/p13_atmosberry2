import binascii
import os

from django.contrib.auth import get_user_model
from django.urls import reverse
from pytest import mark
from rest_framework.authtoken.models import Token

from api.models import Device
from pages.forms import DeviceForm


@mark.django_db
def test_refresh_token(client):
    user = get_user_model()
    user = user.objects.get(id=1)

    client.force_login(user)
    before = Token.objects.filter(user=user).values("key")
    response = client.post(reverse("pages:refresh"))
    after = Token.objects.filter(user=user).values("key")

    assert len(after[0].get("key")) != before[0].get("key")


@mark.django_db
def test_refresh_token_bad_request(client):
    user = get_user_model()
    user = user.objects.get(id=1)

    client.force_login(user)
    response = client.get(reverse("pages:refresh"))

    assert response.status_code == 404


@mark.parametrize(
    "device, lon, lat",
    [
        ("rasp", 42.5, 1.2),
        ("Raspberry zero v1.2", 124.5, 32.2),
    ],
)
@mark.django_db
def test_add_device_form_valid(device, lon, lat):
    """ A valid form : with or without place """

    valid_form = DeviceForm(
        data={
            "device": device,
            "lat": lat,
            "lon": lon,
        }
    )
    assert valid_form.is_valid()


@mark.parametrize(
    "device, lon, lat",
    [
        ("Raspberry zero v1.2", 124.5, 32.2),
    ],
)
@mark.django_db
def test_add_device(client, device, lon, lat):
    payload = {"device": device, "lat": lat, "lon": lon}

    user = get_user_model()
    user = user.objects.get(id=1)

    client.force_login(user)

    response = client.post(reverse("pages:add_device"), payload)

    qs = Device.objects.filter(user=user).values("name")
    all_name_device = [device, "raspberry_device"]
    assert response.status_code == 200
    for element in qs:
        assert element.get("name") in all_name_device
