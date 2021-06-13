from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from .models import Curso, Clase
from .forms import ClaseForm
from alumno.models import Alumno
# Create your views here.


def ListaClaseCurso(request):
    user= request.user
    if user.is_authenticated:
        if user.tipo_usuario=='DC':
            curso= Curso.objects.all().get(docente=user.id)
            clases= Clase.objects.all().filter(curso=curso.IdCurso)
            return render(request,'curso/clases_curso.html',{'clases': clases,'curso':curso})
        elif user.tipo_usuario=='AP':
            alumno= Alumno.objects.all().get(apoderado=user.id)
            clases= Clase.objects.all().filter(curso=alumno.curso.IdCurso)
            return render(request,'curso/clases_curso.html',{'clases': clases,'curso':alumno.curso})
        else:
            return render(request,'core/prueba.html')
    else:
        return render(request,'core/login_required.html')

def CrearClase(request):
    user=request.user
    if user.is_authenticated:
        if user.tipo_usuario=='DC':
            curso= Curso.objects.all().filter(docente=user.id)[0]
            form=ClaseForm(request.POST)
            if form.is_valid():
                form.save()
                HttpResponseRedirect("/curso")
            return render(request,'curso/crear_clase.html',{'form':form})
        else: 
            return render(request,'core/prueba.html')


    else:
        return render(request,'core/login_required.html')

def EditarClase(request,id):
    user=request.user
    if user.is_authenticated:
        if user.tipo_usuario=='DC':

            obj=get_object_or_404(Clase,IdClase=id)

            form= ClaseForm(request.POST, instance =obj)

            if form.is_valid():
                form.save()
                HttpResponseRedirect("/")
            return render(request,'curso/actualizar_clase.html',{'form':form})
        else: 
            return render(request,'core/prueba.html')

    else:
        return render(request,'core/login_required.html')

def EliminarClase(request,id):
    user=request.user
    if user.is_authenticated:
        if user.tipo_usuario=='DC':

            obj=get_object_or_404(Clase,IdClase=id)


            if request.method=="POST":
                obj.delete()
                HttpResponseRedirect("/")
            return render(request,'curso/eliminar_clase.html')
        else: 
            return render(request,'core/prueba.html')

    else:
        return render(request,'core/login_required.html')
        