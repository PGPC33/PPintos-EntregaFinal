from django.contrib import admin
from . import models

admin.site.register(models.Post)
admin.site.register(models.TemaPost)
# admin.site.register(models.Publicacion)


@admin.register(models.Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "texto", "tema", "fecha_publicacion")
    search_fields = ("titulo", "texto", "tema", "fecha_publicacion")
    ordering = ("fecha_publicacion",)
