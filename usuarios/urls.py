from django.urls import path
from . import views

urlpatterns = [
    # Profes
    path("profesores/", views.profesores, name="Profesores"),
    path("nuevo_profesor/", views.nuevo_profesor, name="NuevoProfesor"),
    path("profesor/<id>", views.ver_profesor, name="VerProfesor"),
    path("profesor/editar/<id>", views.editar_profesor, name="EditarProfesor"),
    path("profesor/eliminar/<id>", views.eliminar_profesor, name="EliminarProfesor"),
    # Estudiantes
    path("estudiantes/", views.ListarEstudiantes.as_view(), name="Estudiantes"),
    path("nuevo_estudiante/", views.CrearEstudiante.as_view(), name="NuevoEstudiante"),
    path("estudiante/<pk>", views.VerEstudiante.as_view(), name="VerEstudiante"),
    path("estudiante/editar/<pk>", views.EditarEstudiante.as_view(), name="EditarEstudiante"),
    path("estudiante/eliminar/<pk>", views.BorrarEstudiante.as_view(), name="EliminarEstudiante"),
]
