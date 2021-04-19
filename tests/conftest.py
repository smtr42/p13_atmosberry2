from pytest import fixture

from django.test import Client
from django.core.management import call_command


@fixture
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'fixture_data.json')


@fixture
def client_anon():
    """ Provide a Django test client with anonymous (unconnected) """
    return Client()
