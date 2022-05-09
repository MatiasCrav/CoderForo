from django.shortcuts import render
from django.http import HttpResponse
from .models import Hilo


def inicio(request):
    return render(request, "paginas/inicio.html")


def buscar_comision(request, comision):
    if request.GET.get("titulo"):
        titulo = request.GET.get("titulo")
        hilos = Hilo.objects.filter(titulo__icontains=titulo, comision=comision)
        return render(request, "paginas/resultado_buscar.html", {"hilos": hilos})

    return render(request, "paginas/buscar.html")
