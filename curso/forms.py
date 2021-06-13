from django import forms
from .models import Curso, Clase

class ClaseForm(forms.ModelForm):
    class Meta:
        model=Clase
        fields='__all__'
        #exclude=['curso',]