from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=150, blank=True, null=True, unique=True)
    last_name = models.CharField(max_length=150, blank=True, null=True, unique=True)
    email = models.EmailField(_("email address"), unique=True)