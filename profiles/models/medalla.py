from django.db import models


class Medalla(models.Model):
    title = models.CharField(max_length=50);
    image = models.ImageField(upload_to="medallas", blank='')
    puntos = models.IntegerField(default=0)
