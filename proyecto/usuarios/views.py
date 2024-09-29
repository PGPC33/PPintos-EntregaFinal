from django.shortcuts import render
from .forms import UsuarioForm
from .models import Usuario


def index(request):
    return render(request, "usuarios/index.html")


def usuario_list(request):
    usuarios = Usuario.objects.all()
    contexto = {"usuarios": usuarios}
    return render(request, "usuarios/usuario_list.html", contexto)


def usuario_create(request):
    if request.method == "GET":
        form = UsuarioForm()
    if request.method == "POST":
        form = UsuarioForm(request.POST)
    return render(request, "usuarios/usuario_create.html", {"form": form})
    """Se elimina la variable contexto"""
