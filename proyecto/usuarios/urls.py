from django.urls import path
from . import views

# nombre global
app_name = "usuarios"


# nombre local
urlpatterns = [
    path("", views.index, name="index"),
    path("usuario/list", views.usuario_list, name="usuario_list"),
]
