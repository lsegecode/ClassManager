from django import forms
from .models import Alumno


class AlumnoForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(AlumnoForm, self).__init__(*args, **kwargs)
        self.fields['fecha_nac'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )
        self.fields['copiaDNI_A'].required = False
        self.fields['fecha_nac'].required = True


    dni_a = forms.CharField(label="DNI")
    cuil_a = forms.CharField(label="CUIL")
    apellido_a = forms.CharField(label="Apellido del alumno")
    nombre_a = forms.CharField(label="Nombre del alumno")
    copiaDNI_A = forms.ImageField(label="Copia de DNI")
    fecha_nac = forms.ImageField(label="Fecha de Nacimiento")

    class Meta:
        model = Alumno
        fields = ['id_alumno', 'dni_a', 'cuil_a',
                  'apellido_a', 'nombre_a', 'matricula', 
                  'tutores', 'telefono', 'direccion', 
                  'fecha_nac', 'copiaDNI_A', 'id_curso']
    

class AlumnoFormUpdate(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AlumnoFormUpdate, self).__init__(*args, **kwargs)
        self.fields['fecha_nac'].widget = forms.widgets.DateInput(
            attrs={
                'type': 'date', 'placeholder': 'yyyy-mm-dd (DOB)',
                'class': 'form-control'
                }
            )
        self.fields['copiaDNI_A'].required = False
        self.fields['fecha_nac'].required = True

       
    dni_a = forms.CharField(label="DNI")
    cuil_a = forms.CharField(label="cuil_a")
    apellido_a = forms.CharField(label="Apellido del alumno")
    nombre_a = forms.CharField(label="Nombre del alumno")
    copiaDNI_A = forms.CharField(label="Copia de DNI")    
    fecha_nac = forms.ImageField(label="Fecha de Nacimiento")
    
    class Meta:
        model = Alumno
        fields = ['id_alumno', 'dni_a', 'cuil_a',
                  'apellido_a', 'nombre_a', 'matricula', 
                  'tutores', 'telefono', 'direccion', 
                  'fecha_nac', 'copiaDNI_A', 'id_curso']
