from django.shortcuts import render
from .models import Hilo
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test


def inicio(request):
    return render(request, "paginas/inicio.html")


def buscar_comision(request, comision):
    if request.GET.get("titulo"):
        titulo = request.GET.get("titulo")
        hilos = Hilo.objects.filter(titulo__icontains=titulo, comision=comision)
        return render(request, "paginas/resultado_buscar.html", {"hilos": hilos})

    return render(request, "paginas/buscar.html")


# Crear hilo: solo puede un profesor logueado
class ListarHilos(UserPassesTestMixin, ListView):
    model = Hilo
    template_name = "paginas/hilos.html"

    # Solo puedo acceder cuando test_func devuelve true
    def test_func(self):
        print(self.request.user.is_authenticated)
        return True

    # Cuáles son los objetos que traigo de la BD
    def get_queryset(self):
        # usuario: en self.request.user
        # parametros de la url: en self.kwargs["parametro"]
        return super().get_queryset()

    # Lo que se envía al contexto
    def get_context_data(self):
        return super().get_context_data()


# Cuando la funcion devuelve True puedo acceder a la view
def funcio_de_test(user):
    return True
# Quiero acceder cuando esta logueado como profe
@user_passes_test(funcio_de_test)
def nuevo_hilo(request):
    ...


# Editar hilo: solo puede un profesor o el autor original

# Borrar hilo: solo puede un profesor o el autor original
