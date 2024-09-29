from django.shortcuts import render
from .forms import TemaPostForm, PostForm
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


def temapost_create(request):
    if request.method == "GET":
        form = TemaPostForm()
    if request.method == "POST":
        form = TemaPost(request.POST)
    return render(request, "posts/temapost_create.html", {"form": form})
    """Se elimina la variable contexto"""


def post_create(request):
    if request.method == "GET":
        form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
    return render(request, "posts/post_create.html", {"form": form})
    """Se elimina la variable contexto"""
