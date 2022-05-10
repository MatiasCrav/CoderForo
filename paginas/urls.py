from django.urls import path
from . import views

urlpatterns = [
    path("buscar/<comision>", views.buscar_comision, name="BuscarHilo"),
    path("hilos/", views.ListarHilos.as_view(), name="Hilos")
]
