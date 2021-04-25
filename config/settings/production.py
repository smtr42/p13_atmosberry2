from . import *

DEBUG = False
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env('ALLOWED_HOSTS')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env('DATABASE_NAME'),
        "USER": env('DATABASDATABASE_USERE_NAME'),
        "PASSWORD": env('DATABASE_PASS'),
        "HOST": env('DATABASE_HOST'),
        "PORT": "5432",
    }
}
