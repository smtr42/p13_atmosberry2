"""Forms lined to the custom user."""
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """A form to create data."""

    class Meta:
        model = CustomUser
        fields = ("username", "email")


class CustomUserChangeForm(UserChangeForm):
    """A form to change data."""

    class Meta:
        model = CustomUser
        fields = ("username", "email")
