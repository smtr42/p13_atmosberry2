import uuid

from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import Client
from pytest import fixture
from rest_framework.test import APIClient


@fixture(scope="module")
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command("loaddata", "fixture_data.json")


@fixture
def client_anon():
    """Provide a Django test client with anonymous (unconnected)"""
    return Client()


@fixture
def api_client():
    return APIClient()


@fixture
def test_password():
    return "strong-test-pass"


@fixture
def create_user(db, test_password):
    def make_user(**kwargs):
        user = get_user_model()
        kwargs["password"] = test_password
        if "username" not in kwargs:
            kwargs["username"] = str(uuid.uuid4())
        return user.objects.create_user(**kwargs)

    return make_user
