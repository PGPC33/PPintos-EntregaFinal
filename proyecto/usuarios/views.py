from django.shortcuts import render
from .models import Post, Usuario


def post_list(request):
    posts = Post.objects.all()
    contexto = {"posts": posts}
    return render(request, "usuarios/post_list.html", contexto)
