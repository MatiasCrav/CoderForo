from django.db import models
from django.contrib.auth.models import User


class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField()
    web = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    comision = models.IntegerField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"[Profe] {self.nombre} {self.apellido}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField()
    cursos_completados = models.IntegerField(blank=True, default=0)
    descripcion = models.TextField(blank=True, null=True)
    comision = models.IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
            return f"[Estudiante] {self.nombre} {self.apellido}"