from django import forms
from .models import Personal


class PersonalForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_nac_p'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
            }
        )

    class Meta:
        model = Personal
        fields = ['id_personal', 'dni_p', 'cuil_p', 'apellido_p', 'nombre_p',
                  'legajo_p', 'telefono_p', 'direccion_p', 'fecha_nac_p', 'copiaDNI_p', 'rol_p', 'id_materia']


class PersonalFormUpdate(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fecha_nac_p'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
            }
        )

    class Meta:
        model = Personal
        fields = ['id_personal', 'dni_p', 'cuil_p', 'apellido_p', 'nombre_p',
                  'legajo_p', 'telefono_p', 'direccion_p', 'fecha_nac_p', 'copiaDNI_p', 'rol_p', 'id_materia']
