from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


def index(request):
    return render(request, "main/index.html")


class Register(CreateView):
    form_class = CustomUserCreationForm
    template_name = "main/register.html"
    success_url = reverse_lazy("main: login")
