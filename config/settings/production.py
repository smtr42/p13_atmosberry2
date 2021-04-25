from . import *

DEBUG = False
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = [env("IP"), "localhost", "192.168.0.1", env("URL1"), env("URL2")]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASS"),
        "HOST": env("DATABASE_HOST"),
        "PORT": "5432",
    }
}
