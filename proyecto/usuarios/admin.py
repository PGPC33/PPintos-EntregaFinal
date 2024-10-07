from django.contrib import admin
from . import models

# admin.site.register(models.Usuario)


@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nombre", "apellido", "user")
    search_fields = ("nombre", "apellido", "user")
    ordering = ("nombre", "apellido")
    # list_filter = ("")
    # date_hierarchy= "nacimiento"
