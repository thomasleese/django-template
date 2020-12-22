from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = None
    last_name = None
    full_name = models.CharField(_("full name"), max_length=60, blank=True)

    def __str__(self):
        return self.full_name or self.username

    def get_full_name(self):
        return self.full_name

    def get_short_name(self):
        return self.username
