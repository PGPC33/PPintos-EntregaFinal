from django import forms
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["nombre", "apellido", "user", "password"]

    def clean_nombre(self):
        nombre: str = self.cleaned_data.get("nombre", "")
        if not nombre:
            raise ValidationError("El nombre no puede estar vacío")
            if len(nombre) > 50:
                raise ValidationError("El nombre no puede tener más de 50 caracteres")
        return nombre
