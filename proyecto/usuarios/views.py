from django.shortcuts import render
from .models import Post, Usuario


def index(request):
    return render(request, "usuarios/index.html")


def post_list(request):
    posts = Post.objects.all()
    contexto = {"posts": posts}
    return render(request, "usuarios/post_list.html", contexto)


def usuario_list(request):
    usuarios = Usuario.objects.all()
    contexto = {"usuarios": usuarios}
    return render(request, "usuarios/usuario_list.html", contexto)
