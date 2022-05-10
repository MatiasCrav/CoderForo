from django.db import models

class Profesor(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField()
    web = models.CharField(max_length=255, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    comision = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"[Profe] {self.nombre} {self.apellido}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField()
    cursos_completados = models.IntegerField()
    descripcion = models.TextField()
    comision = models.IntegerField()

    def __str__(self):
            return f"[Estudiante] {self.nombre} {self.apellido}"