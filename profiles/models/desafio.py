from django.db import models


class Desafio(models.Model):
    titulo = models.CharField(max_length=150)
    tiempo = models.CharField(max_length=150)
