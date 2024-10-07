from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

# nombre global
app_name = "usuarios"


# nombre local
urlpatterns = [
    path("", views.index, name="index"),
    path("usuario/list", login_required(views.usuario_list), name="usuario_list"),
    path("usuario/create", login_required(views.usuario_create), name="usuario_create"),
    path(
        "usuario/detail/<int:pk>",
        login_required(views.usuario_detail),
        name="usuario_detail",
    ),
    path(
        "usuario/update/<int:pk>",
        login_required(views.usuario_update),
        name="usuario_update",
    ),
    path(
        "usuario/delete/<int:pk>",
        login_required(views.usuario_delete),
        name="usuario_delete",
    ),
]
