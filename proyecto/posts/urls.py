from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views

# nombre global
app_name = "posts"

# nombre local
urlpatterns = [
    path("", views.index, name="index"),
    path("temapost/list", login_required(views.temapost_list), name="temapost_list"),
    path(
        "temapost/create", login_required(views.temapost_create), name="temapost_create"
    ),
    path("post/list", login_required(views.post_list), name="post_list"),
    # ejemplo con views Django
    # path("temapost/list", views.TemaPostList.as_view(), name="temapost_list"),
    path("post/create", login_required(views.post_create), name="post_create"),
]
