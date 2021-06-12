from django.db import models
from django.conf import settings
from core.models import User
# Create your models here.

#aqui va el modelo de curso y de clase/actividades

class Curso(models.Model):
    IdCurso= models.AutoField(primary_key=True)
    nombre= models.CharField(max_length=50)
    enlace= models.URLField(blank=True, null=True)
    docente= models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name="Curso"
        verbose_name_plural="Cursos"

    def __str__(self):
        return self.nombre

class Clase(models.Model):
    IdClase= models.AutoField(primary_key=True)
    titulo= models.CharField(max_length=30)
    descripcion= models.TextField(blank=True, null=True)
    curso= models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True, verbose_name = "Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name = "Última actualización")

    class Meta:
        verbose_name="Clase"
        verbose_name_plural="Clases"
        ordering = ["-created"]

    def __str__(self):
        return self.titulo