from django.urls import path
from . import views

urlpatterns = [
    path("post/list", views.post_list),
    path("usuario/list", views.usuario_list),
]
