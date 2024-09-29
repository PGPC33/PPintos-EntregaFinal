from django.urls import path
from . import views

# nombre global
app_name = "posts"

# nombre local
urlpatterns = [
    path("", views.index, name="index"),
    path("temapost/list", views.temapost_list, name="temapost_list"),
    path("temapost/create", views.temapost_create, name="temapost_create"),
    path("post/list", views.post_list, name="post_list"),
    path("post/create", views.post_create, name="post_create"),
]
