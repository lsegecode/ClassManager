from django import forms
from .models import Especialidad

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['id_especialidad', 'nombreEspecialidad', 'disenioCurricular', 'cantidadMaterias']

class EspecialidadFormUpdate(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['id_especialidad', 'nombreEspecialidad', 'disenioCurricular', 'cantidadMaterias']