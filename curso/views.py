from django.shortcuts import render
from .models import Curso, Clase
from .forms import CrearClaseForm

# Create your views here.


def ListaClaseCurso(request):
    user= request.user
    if user.is_authenticated:
        if user.tipo_usuario=='DC':
            curso= Curso.objects.all().filter(docente=user.id)[0]
            clases= Clase.objects.all().filter(curso=curso.IdCurso)
            return render(request,'curso/clases_curso.html',{'clases': clases,'curso':curso})
        else:
            return render(request,'core/prueba.html')
    else:
        return render(request,'core/login_required.html')

def CrearClase(request):
    user=request.user
    if user.is_authenticated:
        if user.tipo_usuario=='DC':
            curso= Curso.objects.all().filter(docente=user.id)[0]
            print ('este es request')
            print (request.POST)
            form= CrearClaseForm(request.POST)
            print('este es el form')
            print (form)
            form.curso=curso.IdCurso
            if form.is_valid():
                form.save()
            return render(request,'curso/crear_clase.html',{'form':form})
        else: 
            return render(request,'core/prueba.html')


    else:
        return render(request,'core/login_required.html')