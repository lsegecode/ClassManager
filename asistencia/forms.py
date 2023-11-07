from django import forms
from .models import Asistencia

from alumnado.models import Alumno

class AsistenciaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fechaA'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )

    class Meta:
        model = Asistencia
        fields = ['id_alumno', 'fechaA', 'condicion', 'cantidadA', 'turno', 'reintegrado', 'evento']
    
class AsistenciaFormUpdate(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = ['id_alumno', 'fechaA', 'condicion', 'cantidadA', 'turno', 'reintegrado', 'evento']
