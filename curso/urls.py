from django.urls import path

from .views import ListaClaseCurso, CrearClase

urlpatterns = [
    path('', ListaClaseCurso, name='curso'),
    path('crearclase', CrearClase, name='crear_clase')
]