from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField()
    web = models.CharField(max_length=255)
    descripcion = models.TextField()
    comision = models.IntegerField()


class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField()
    web = models.CharField(max_length=255)
    descripcion = models.TextField()
    comision = models.IntegerField()

