from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="InicioPags"),
    path("buscar/<comision>", views.buscar_comision, name="BuscarHilo"),
]