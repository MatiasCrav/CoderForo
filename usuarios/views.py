from urllib.request import Request
from django.shortcuts import render, redirect

from usuarios.models import Profesor
from .forms import FormProfesor


def inicio(request):
    return render(request, "usuarios/inicio.html")


def nuevo_profesor(request):
    if request.method == "POST":
        mi_form = FormProfesor(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data
            profe = Profesor(
                nombre=info["nombre"],
                apellido=info["apellido"],
                email=info["email"],
                web=info["web"],
                descripcion=info["descripcion"],
                comision=info["comision"],
            )
            profe.save()
            return redirect("InicioUsuarios")

    mi_form = FormProfesor()

    return render(request, "usuarios/formProfesores.html", {"form": mi_form})
