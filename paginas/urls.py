from django.urls import path
from . import views

urlpatterns = [
    path("buscar/<comision>", views.buscar_comision, name="BuscarHilo"),
]
