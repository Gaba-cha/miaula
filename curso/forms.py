from django import forms
from .models import Curso, Clase

class CrearClaseForm(forms.ModelForm):
    class Meta:
        model=Clase
        exclude=['curso',]