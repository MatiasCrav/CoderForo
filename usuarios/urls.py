from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="InicioUsuarios"),
    path("nuevo_profesor", views.nuevo_profesor, name="NuevoProfesor"),
]