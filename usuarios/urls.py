from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="InicioUsuarios"),
    path("profesores", views.profesores, name="Profesores"),
    path("nuevo_profesor", views.nuevo_profesor, name="NuevoProfesor"),
    path("profesor/<id>", views.ver_profesor, name="VerProfesor"),
    path("profesor/editar/<id>", views.editar_profesor, name="EditarProfesor"),
    path("profesor/eliminar/<id>", views.eliminar_profesor, name="EliminarProfesor"),
]