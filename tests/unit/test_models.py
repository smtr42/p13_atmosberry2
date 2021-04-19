from pytest import mark

from django.urls import reverse
from api.models import Device


@mark.django_db
def test_1():
    device = Device.objects.all()
    print(device)
    assert device.__str__() == "Mise à jour complète du parc vers win10"
