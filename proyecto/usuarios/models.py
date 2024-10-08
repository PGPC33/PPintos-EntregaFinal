from django.db import models


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    user = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    #post_id = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
