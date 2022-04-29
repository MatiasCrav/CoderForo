from django.db import models


class Hilo(models.Model):
    titulo = models.CharField(max_length=255)
    tema = models.CharField(max_length=255)
    contenido = models.TextField()
    comision = models.IntegerField()
    posteador = models.CharField(max_length=255)
