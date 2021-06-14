
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    #path('', include('alumno.urls')),
    #path('', include('apoderado.urls')),
    path('curso/', include('curso.urls')),
    #path('', include('docente.urls')),

    #path autenticacion
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
]
