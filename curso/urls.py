from django.urls import path

from .views import ListaClaseCurso, CrearClase, EditarClase, EliminarClase

urlpatterns = [
    path('', ListaClaseCurso, name='curso'),
    path('crearclase', CrearClase, name='crear_clase'),
    path('<id>/editar', EditarClase, name='editar_clase'),
    path('<id>/eliminar', EliminarClase, name='eliminar_clase'),

]