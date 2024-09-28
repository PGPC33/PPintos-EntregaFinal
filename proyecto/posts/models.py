from django.db import models


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.CharField(max_length=500)
    # img= models.ImageField(upload_to='images/')

    def __str__(self):
        return self.titulo


class TemaPost(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name: "Tema"
        verbose_naem_plural: "Temas"
