from django import forms
from .models import Notas

class NotasForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fechaNota'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )

    class Meta:
        model = Notas
        fields = ['id_nota', 'valor', 'instancia', 'fechaNota',  'AnnioCursada', 'id_materia', 'id_alumno']


class NotasFormUpdate(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fechaNota'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )

    class Meta:
        model = Notas
        fields = ['id_nota', 'valor', 'instancia', 'fechaNota', 'AnnioCursada', 'id_materia', 'id_alumno']
