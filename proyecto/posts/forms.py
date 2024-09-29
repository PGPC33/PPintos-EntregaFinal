from django import forms
from .models import TemaPost, Post


class TemaPostForm(forms.ModelForm):
    class Meta:
        model = TemaPost
        fields = ["tema"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["titulo", "texto", "tema"]
