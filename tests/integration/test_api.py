import json
from datetime import datetime

import pytz
from django.urls import reverse
from pytest import mark
from rest_framework.authtoken.models import Token

from api.models import Device, Sensor


@mark.django_db
def test_unauthorized_request(api_client):
    print(api_client)
    url = reverse("data")
    response = api_client.get(url)
    assert response.content == b"[]"


@mark.django_db
def test_authorized_request(api_client):
    url = reverse("data")
    token, _ = Token.objects.get_or_create(user_id=1)
    api_client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
    response = api_client.get(url)
    assert response.status_code == 200


@mark.django_db
def test_get_endpoint(api_client):
    """URL access for visitor and checks templates."""
    response = api_client.get(reverse("api_index"))
    data = json.loads(response.content)
    assert response.status_code == 200
    assert len(json.loads(response.content)) == 1
    assert data == [
        {
            "name": "BMP_280",
            "timestamp": "2021-04-07T09:32:50.998000Z",
            "measure": 12.2,
            "sensor_type": "T",
        }
    ]


@mark.django_db
def test_get_loc(api_client):
    """URL access for visitor and checks templates."""
    response = api_client.get(reverse("loc"))
    data = json.loads(response.content)
    assert response.status_code == 200
    assert len(json.loads(response.content)) == 1
    assert data == [{"lat": "48.862725", "lon": "2.287592", "user": 1}]


@mark.django_db
def test_get_data(api_client):
    """URL access for visitor and checks templates."""

    date = datetime.utcnow().replace(tzinfo=pytz.utc)

    new_reading = Sensor.objects.create(
        device=Device.objects.get(id=2),
        name="BMP_280",
        timestamp=date,
        measure=24.3,
        sensor_type="T",
    )
    new_reading.save()
    token, _ = Token.objects.get_or_create(user_id=1)
    api_client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
    response = api_client.get(reverse("data"))
    data = json.loads(response.content)
    assert response.status_code == 200
    assert data[0].get("name") == "BMP_280"
    assert data[0].get("measure") == 24.3
