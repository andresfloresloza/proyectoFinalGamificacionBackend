from django.contrib.auth.models import AbstractUser
from django.db import models

from proyectoFinalGamificacionBackend import settings


class CustomerUser(AbstractUser):
    uid = models.CharField(max_length=100, blank=False, unique=True)
    username = models.CharField(max_length=50, blank=False, unique=True)
    email = models.CharField(max_length=100, blank=False, unique=True)
    password = models.CharField("password", max_length=128, blank=True)


