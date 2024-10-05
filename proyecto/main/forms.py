from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


# cada vez que personalizamos algo de django anteponemos custom (personalizando)
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2")
