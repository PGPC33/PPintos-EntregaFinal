from django.shortcuts import render
from .models import TemaPost


# Create your views here.
def index(request):
    return render(request, "posts/index.html")


def post_list(request):
    posts = Post.objects.all()
    contexto = {"posts": posts}
    return render(request, "posts/post_list.html", contexto)
