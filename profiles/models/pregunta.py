from django.db import models

from profiles.models import Tema


class Pregunta(models.Model):
    pregunta = models.CharField(max_length=200);
    respuestaCorrecta = models.CharField(null=False, max_length=200)
    respuestaIncorrecta1 = models.CharField(null=False, max_length=200)
    respuestaIncorrecta2 = models.CharField(null=False, max_length=200)
    respuestaIncorrecta3 = models.CharField(null=False, max_length=200)
    puntos = models.IntegerField(null=False, default=100)
    tema = models.ForeignKey(Tema, on_delete=models.CASCADE)