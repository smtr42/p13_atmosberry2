from datetime import datetime
import pytz

from pytest import fixture, mark

from django.urls import reverse
from api.models import Device, Address, Sensor


@fixture
def index_list_templates():
    return [
        "base.html",
        "pages/index.html",
    ]


@mark.django_db
@mark.parametrize(
    "url, status",
    [("", 200), (reverse("pages:frontpage"), 200)],
)
def test_route_anon_index_urls(client_anon, url, status, index_list_templates):
    """ URL access for visitor and checks templates """
    response = client_anon.get(url)

    assert response.status_code == status
    for template in index_list_templates:
        assert template in [t.name for t in response.templates]
