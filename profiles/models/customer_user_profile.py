from dataclasses import dataclass
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from proyectoFinalGamificacionBackend import settings


@dataclass
class ProfileDto:
    customer_user: int
    full_name: str
    birthday_date: str
    phone_number: str


class CustomerUserProfile(models.Model):
    customer_user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True)
    birthday_date = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="profiles", blank='', default="profiles/icono foto.png")
    puntos = models.IntegerField(default=0)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        CustomerUserProfile.objects.create(customer_user=instance)
