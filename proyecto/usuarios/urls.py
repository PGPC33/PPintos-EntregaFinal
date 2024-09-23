from django.urls import path
from . import views

# nombre global
app_name = "usuarios"


# nombre local
urlpatterns = [
    path("", views.index, name="index"),
    # path("post/list", views.post_list, name="post_list"),
    # path("usuario/list", views.usuario_list, name="usuario_list"),
]
