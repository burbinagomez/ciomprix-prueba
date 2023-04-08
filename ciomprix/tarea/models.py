from django.db import models
from persona.models import Persona

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_limite = models.DateTimeField()
    completada = models.BooleanField(default=False)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='tareas')