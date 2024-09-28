from django.shortcuts import render
from .models import Post, TemaPost


# Create your views here.
def index(request):
    return render(request, "posts/index.html")


def post_list(request):
    posts = Post.objects.all()
    contexto = {"posts": posts}
    return render(request, "posts/post_list.html", contexto)


def temapost_list(request):
    temapost = TemaPost.objects.all()
    contexto = {"temapost": temapost}
    return render(request, "posts/temapost_list.html", contexto)
