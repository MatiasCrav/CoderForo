from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# from django.contrib.auth.decorators import
# from django.contrib.auth.mixins import
from django.contrib.auth.models import User

from usuarios.models import Estudiante, Profesor
from .forms import FormProfesor, FormRegistrarse


def profesores(request):
    profes = Profesor.objects.all()
    return render(request, "usuarios/profesores.html", {"profesores": profes})


def ver_profesor(request, id):
    profe = Profesor.objects.get(id=id)
    return render(request, "usuarios/ver_profesor.html", {"profesor": profe})


# Solo puede un admin o el mismo profesor
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


# Solo puede un admin
def nuevo_profesor(request):
    if request.method == "POST":
        mi_form = FormProfesor(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            pass1 = info.get("password1")
            pass2 = info.get("password2")
            nombre = info.get("nombre")
            apellido = info.get("apellido")
            email = info.get("email")
            data = {
                "username": nombre + apellido,
                "password1": pass1,
                "password2": pass2,
                "email": email,
            }

            form_registro = FormRegistrarse(data)
            if form_registro.is_valid():
                form_registro.save()

                profe = Profesor(
                    nombre=nombre,
                    apellido=apellido,
                    email=email,
                    web=info.get("web"),
                    descripcion=info.get("descripcion"),
                    comision=info.get("comision"),
                )
                profe.save()

                return redirect("Profesores")

    mi_form = FormProfesor()

    return render(request, "usuarios/formProfesores.html", {"form": mi_form})


# Solo puede un admin o el mismo profesor
def eliminar_profesor(request, id):
    profe = Profesor.objects.get(id=id)
    profe.delete()

    return redirect("Profesores")


class ListarEstudiantes(ListView):
    model = Estudiante
    template_name = "usuarios/estudiantes.html"


class CrearEstudiante(CreateView):
    model = Estudiante
    template_name = "usuarios/formEstudiantes.html"
    success_url = "/usuarios/estudiantes/"
    fields = (
        "nombre",
        "apellido",
        "email",
        "cursos_completados",
        "descripcion",
        "comision",
    )


class VerEstudiante(DetailView):
    model = Estudiante
    template_name = "usuarios/ver_estudiante.html"


# Solo puede un admin o el mismo estudiante
class EditarEstudiante(UpdateView):
    model = Estudiante
    template_name = "usuarios/formEstudiantes.html"
    success_url = "/usuarios/estudiantes/"
    fields = (
        "nombre",
        "apellido",
        "email",
        "cursos_completados",
        "descripcion",
        "comision",
    )


# Solo puede un admin o el mismo estudiante
class BorrarEstudiante(DeleteView):
    model = Estudiante
    success_url = "/usuarios/estudiantes/"
