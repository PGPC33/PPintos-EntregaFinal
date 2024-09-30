from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
)
from .forms import TemaPostForm, PostForm
from .models import Post, TemaPost


def index(request):
    return render(request, "posts/index.html")


def post_list(request):
    posts = Post.objects.all()
    contexto = {"posts": posts}
    return render(request, "posts/post_list.html", contexto)


# List
def temapost_list(request):
    query = request.GET.get("query", "")
    if query:
        temapost = TemaPost.objects.filter(nombre__icontains=query)
    else:
        temapost = TemaPost.objects.all()
    contexto = {"temapost": temapost}
    return render(request, "posts/temapost_list.html", contexto)


class TemaPostList(ListView):
    model = TemaPost
    # template_name = "posts/temapost_list.html"
    # context_object_name = "temapost"
    queryset = TemaPost.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        q = request.GET.GET("q")
        if q:
            queryset = TemaPost.objects.filter(nombre__icontains=q)
            return queryset


# Create
def temapost_create(request):
    if request.method == "GET":
        form = TemaPostForm()

    if request.method == "POST":
        form = TemaPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:temapost_list")
    return render(request, "posts/temapost_create.html", {"form": form})
    """Se elimina la variable contexto"""


# Create
def post_create(request):
    if request.method == "GET":
        form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:post_list")
    return render(request, "posts/post_create.html", {"form": form})
    """Se elimina la variable contexto"""
