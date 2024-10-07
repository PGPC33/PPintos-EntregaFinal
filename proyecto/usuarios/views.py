from django.shortcuts import render, redirect

# from django.contrib.auth.decorators import login_required
from .forms import UsuarioForm
from .models import Usuario


def index(request):
    return render(request, "usuarios/index.html")


# @login_required
def usuario_list(request):
    usuarios = Usuario.objects.all()
    contexto = {"usuarios": usuarios}
    return render(request, "usuarios/usuario_list.html", contexto)


def usuario_create(request):
    if request.method == "GET":
        form = UsuarioForm()
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuarios:usuario_list")
    return render(request, "usuarios/usuario_create.html", {"form": form})
    """Se elimina la variable contexto"""


def usuario_detail(request, pk: int):
    query = Usuario.objects.get(id=pk)
    context = {"usuario": query}
    return render(request, "usuarios/usuario_detail.html", context)


def usuario_update(request, pk: int):
    query = Usuario.objects.get(id=pk)
    if request.method == "GET":
        form = UsuarioForm(instance=query)

    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("usuarios:usuario_list")
    return render(request, "usuarios/usuario_create.html", {"form": form})


def usuario_delete(request, pk: int):
    query = Usuario.objects.get(id=pk)
    context = {"usuario": query}
    if request.method == "POST":
        query.delete()
        return redirect("usuarios:usuario_list")
    return render(request, "usuarios/usuario_confirm_delete.html", context)
