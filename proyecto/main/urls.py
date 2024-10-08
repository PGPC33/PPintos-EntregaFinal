from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


app_name = "main"

urlpatterns = [
    path("", views.index, name="index"),
    path("login", LoginView.as_view(template_name="main/login.html"), name="login"),
    path("logout", LogoutView.as_view(template_name="main/logout.html"), name="logout"),
    path(
        "register",
        views.Register.as_view(template_name="main/register.html"),
        name="register",
    ),
]
