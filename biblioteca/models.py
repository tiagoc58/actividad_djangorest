from django.db import models

# Create your models here.
from django.db import models
from django.core.exceptions import ValidationError

def validar_nombre(nombre):
    if nombre.strip() == "":
        raise ValidationError("Hola papu, esto no se puede papu :v")
    
def validar_resumen(resumen):
    if len(resumen) <= 50:
        raise ValidationError("Hola papu, esto es muy pequeño papu 7u7")
    
def validar_resena(resena):
    if resena < 0 or 5 < resena:
        raise ValidationError("Hola papu, rango incorrecto papu UnU")

class Autor(models.Model):
    nombre = models.CharField(max_length=100, validators=[validar_nombre])
    nacionalidad = models. CharField(max_length=100)
    edad = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models. ForeignKey (Autor, on_delete=models.CASCADE, related_name='libros')
    fecha_publicacion = models.DateField()
    resumen = models.TextField(validators=[validar_resumen])
    
    def __str__(self):
        return self.titulo
    
class Resena (models.Model):
    libro = models. ForeignKey (Libro, on_delete=models.CASCADE, related_name='resenas')
    texto = models.TextField()
    calificacion = models. IntegerField(validators=[validar_resena])
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.libro.titulo} - {self.calificacion}/5"
