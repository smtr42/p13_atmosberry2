"""Models for the accounts apps, where is defined a customn user."""
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Creating a custom User for easier evolution."""

    pass

    def __str__(self):
        return self.username
