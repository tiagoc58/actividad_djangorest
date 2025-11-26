from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ["nombre", "nacionalidad", "edad"]
    search_fields = ["nombre", "nacionalidad", "edad"]

@admin.register(models.Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autor", "fecha_publicacion", "resumen"]
    search_fields = ["titulo", "autor__nombre", "fecha_publicacion", "resumen"]

@admin.register(models.Resena)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ["libro", "texto", "calificacion", "fecha"]
    search_fields = ["libro__titulo", "texto", "calificacion", "fecha"]