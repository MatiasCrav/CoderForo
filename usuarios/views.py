from unicodedata import name
from urllib.request import Request
from django.shortcuts import render, redirect

from usuarios.models import Estudiante, Profesor
from .forms import FormProfesor


def inicio(request):
    return render(request, "usuarios/inicio.html")


def profesores(request):
    profes = Profesor.objects.all()
    return render(request, "usuarios/profesores.html", {"profesores": profes})


def ver_profesor(request, id):
    profe = Profesor.objects.get(id=id)
    return render(request, "usuarios/ver_profesor.html", {"profesor": profe})


def editar_profesor(request, id):
    profe = Profesor.objects.get(id=id)

    if request.method == "POST":
        mi_form = FormProfesor(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            profe.nombre = info["nombre"]
            profe.apellido = info["apellido"]
            profe.email = info["email"]
            profe.web = info["web"]
            profe.descripcion = info["descripcion"]
            profe.comision = info["comision"]

            profe.save()
            return redirect("Profesores")

    mi_form = FormProfesor(
        initial={
            "nombre": profe.nombre,
            "apellido": profe.apellido,
            "email": profe.email,
            "web": profe.web,
            "descripcion": profe.descripcion,
            "comision": profe.comision,
        }
    )

    return render(request, "usuarios/formProfesores.html", {"form": mi_form})


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
            return redirect("Profesores")

    mi_form = FormProfesor()

    return render(request, "usuarios/formProfesores.html", {"form": mi_form})


def eliminar_profesor(request, id):
    profe = Profesor.objects.get(id=id)
    profe.delete()

    return redirect("Profesores")
