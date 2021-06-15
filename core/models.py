from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='user/%Y/%m/%d')
    rut= models.CharField(max_length=10, unique=True)
    TIPO_DE_USUARIO_CHOICES=[
        ('DC','Docente'),
        ('AP','Apoderado'),
        ('AD','Administrador')
    ]
    tipo_usuario= models.CharField(max_length=2, choices=TIPO_DE_USUARIO_CHOICES, default='AD')
    especialidad= models.CharField(max_length=20, blank=True, null=True)


    def getTipoUsuario(self):
        return self.tipo_usuario