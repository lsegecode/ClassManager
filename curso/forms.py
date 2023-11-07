from django import forms
from .models import Curso

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['id_curso', 'Annio', 'Division', 'id_materia']

class CursoFormUpdate(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['id_curso', 'Annio', 'Division', 'id_materia']