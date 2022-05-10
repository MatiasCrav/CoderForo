from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.core.exceptions import ObjectDoesNotExist

from usuarios.models import Estudiante, Profesor
from .forms import FormProfesor, FormRegistrarse, FormEstudiante


def profesores(request):
    profes = Profesor.objects.all()
    return render(request, "usuarios/profesores.html", {"profesores": profes})


def ver_profesor(request, id):
    profe = Profesor.objects.get(id=id)
    return render(request, "usuarios/ver_profesor.html", {"profesor": profe})


def es_admin_o_profe(user):
    if not user.is_authenticated:
        return False

    if user.is_staff:
        return True

    try:
        profe = Profesor.objects.get(usuario=user.id)
    except ObjectDoesNotExist:
        profe = None

    return profe is not None


# Solo puede un admin o el mismo profesor
@user_passes_test(es_admin_o_profe)
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


def es_admin(user):
    return user.is_authenticated and user.is_staff


# Solo puede un admin
@user_passes_test(es_admin)
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
            username = nombre + apellido
            data = {
                "username": username,
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
                    usuario=User.objects.get(username=username),
                )
                profe.save()

                return redirect("Profesores")
            else:
                print(form_registro.errors)

    mi_form = FormProfesor()

    return render(request, "usuarios/formProfesores.html", {"form": mi_form})


# Solo puede un admin o el mismo profesor
@login_required
def eliminar_profesor(request, id):
    if request.user.is_staff or request.user.id == id:
        profe = Profesor.objects.get(id=id)
        profe.delete()

        return redirect("Profesores")
    else:
        # redirect("Login")
        redirect("Inicio")


class ListarEstudiantes(ListView):
    model = Estudiante
    template_name = "usuarios/estudiantes.html"


def nuevo_estudiante(request):
    if request.method == "POST":
        mi_form = FormEstudiante(request.POST)
        if mi_form.is_valid():
            info = mi_form.cleaned_data

            pass1 = info.get("password1")
            pass2 = info.get("password2")
            nombre = info.get("nombre")
            apellido = info.get("apellido")
            email = info.get("email")
            username = nombre + apellido
            data = {
                "username": username,
                "password1": pass1,
                "password2": pass2,
                "email": email,
            }

            form_registro = FormRegistrarse(data)
            if form_registro.is_valid():
                form_registro.save()

                estu = Estudiante(
                    nombre=nombre,
                    apellido=apellido,
                    email=email,
                    cursos_completados=info.get("cursos_completados"),
                    descripcion=info.get("descripcion"),
                    comision=info.get("comision"),
                    usuario=User.objects.get(username=username),
                )
                estu.save()

                return redirect("Estudiantes")
            else:
                print(form_registro.errors)

    mi_form = FormEstudiante()

    return render(request, "usuarios/formEstudiantes.html", {"form": mi_form})


class VerEstudiante(DetailView):
    model = Estudiante
    template_name = "usuarios/ver_estudiante.html"


# Solo puede un admin o el mismo estudiante
class EditarEstudiante(UserPassesTestMixin, UpdateView):
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

    # Solo puedo acceder cuando test_func devuelve true
    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_staff or self.request.user.id == self.kwargs["pk"]
        )


# Solo puede un admin o el mismo estudiante
class BorrarEstudiante(UserPassesTestMixin, DeleteView):
    model = Estudiante
    success_url = "/usuarios/estudiantes/"

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_staff or self.request.user.id == self.kwargs["pk"]
        )


def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("Inicio")
    
    return render(request, "usuarios/login.html")


@login_required
def logout_request(request):
    logout(request)
    return redirect("Inicio")