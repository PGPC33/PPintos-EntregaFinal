from django.db import models


class TemaPost(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name: "Tema"
        verbose_naem_plural: "Temas"


class Post(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField(max_length=500)
    tema = models.ForeignKey(
        TemaPost, on_delete=models.SET_NULL, null=True, verbose_name="Tema"
    )
    # img= models.ImageField(upload_to='images/')

    def __str__(self):
        return f"{self.titulo}, {self.texto}, {self.tema}"

    class Meta:
        verbose_name = "Tema"
        verbose_name_plural = "Temas"


class Publicacion(models.Model):
    tema = models.ForeignKey(
        TemaPost,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="tema",
    )
    titulo = models.CharField(max_length=100)
    texto = models.TextField(max_length=500)
    # img= models.ImageField(upload_to='images/')
    fecha_publicacion = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self) -> str:
        return f"{self.titulo}, {self.tema}, {self.texto} {self.fecha_publicacion}"
