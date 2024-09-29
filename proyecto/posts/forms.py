from django import forms
from django.core.exceptions import ValidationError
from .models import TemaPost, Post


class TemaPostForm(forms.ModelForm):
    class Meta:
        model = TemaPost
        fields = ["nombre"]

    def clean_nombre(self):
        nombre: str = self.cleaned_data.get("nombre", "")
        if not nombre.isalpha():
            raise ValidationError("El nombre del tema no puede contener números")
            if len(nombre) < 3 or len(nombre) > 50:
                raise ValidationError(
                    "El nombre del tema no puede ser menor a tres caracteres o máximo 50"
                )
        return nombre


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "texto"]

    def clean_nombre(self):
        titulo: str = self.cleaned_data.get("titulo", "")
        if not titulo.isalpha():
            raise ValidationError("El titulo del post no puede contener números")
            if len(nombre) < 3 or len(nombre) > 50:
                raise ValidationError(
                    "El título del post no puede ser menor a tres caracteres o máximo de 50"
                )
        return titulo
