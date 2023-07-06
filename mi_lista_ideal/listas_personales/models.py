from django.db import models

class Lista(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
class Tarea(models.Model):
    descripcion = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    completado = models.BooleanField(default=False)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.descripcion
