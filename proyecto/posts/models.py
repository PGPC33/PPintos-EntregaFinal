from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=50, unique=True)
    texto = models.CharField(max_length=500)
    # img = models.ImageField(upload_to="images/")

    def __str__(self):
        return f"{self.titulo}"

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
