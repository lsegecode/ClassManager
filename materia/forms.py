from django import forms
from .models import Materia

class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['id_materia', 'nombreMateria', 'id_especialidad']

class MateriaFormUpdate(forms.ModelForm):
    class Meta:
        model = Materia
        fields = ['id_materia', 'nombreMateria', 'id_especialidad']