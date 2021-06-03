from django.db import models
from datetime import date
from curso.models import Curso
from core.models import User
# Create your models here.

# aqui debe ir modelo alumno y el modelo comentario

class Alumno(models.Model):
    rut=models.CharField(max_length=10, primary_key=True)
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=20)
    fecha_nacimiento=models.DateField(editable=True, default=date.today)
    curso= models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
    )
    apoderado=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name= "Alumno"
        verbose_name_plural="Alumnos"

    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Comentario(models.Model):
    IdComentario= models.AutoField(primary_key=True)
    titulo= models.CharField(max_length=30)
    texto=models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Última actualización")
    alumno= models.ForeignKey(
        Alumno,
        on_delete=models.CASCADE,
        default='000-0'
    )

    class Meta:
        verbose_name="Comentario"
        verbose_name_plural="Comentarios"
        ordering=["-created"]
    
    def __str__(self):
        return self.titulo
