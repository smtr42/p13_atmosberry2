from django.contrib.auth import get_user_model
from pytest import mark

from api.models import Address, Device, Sensor


@mark.django_db
def test_user():
    user = get_user_model()
    user = user.objects.get(id=1)
    assert user.__str__() == "loggeduser"


@mark.django_db
def test_device():
    device = Device.objects.get(id=2)
    assert device.__str__() == "raspberry_device"


@mark.django_db
def test_address():
    address = Address.objects.get(id=1)
    assert address.__str__() == "Paris"


@mark.django_db
def test_sensor():
    sensor = Sensor.objects.get(id=1)
    assert sensor.__str__() == "BMP_280"


@mark.django_db
def test_user_create():
    user = get_user_model()
    user.objects.create_user("john", "lennon@thebeatles.com", "johnpassword")
    assert user.objects.count() == 2
