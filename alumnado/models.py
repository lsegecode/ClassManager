from django.db import models
from django.db.models.fields.files import ImageField

# Create your models here.
class Alumno(models.Model):
    id_alumno = models.AutoField(primary_key=True)
    dni_a = models.CharField(max_length=9)
    cuil_a = models.CharField(max_length=15)
    apellido_a = models.CharField(max_length=50)
    nombre_a = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)
    tutores = models.CharField(max_length=100, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.CharField(max_length=50, blank=True)
    fecha_nac = models.DateField()
    copiaDNI_A = ImageField(upload_to='alumnado/images/', blank=True)
    #id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE, blank=True, default=0)

    def __str__(self):
        texto = "{0} {1}({2})"
        return texto.format(self.apellido_a, self.nombre_a, self.id_alumno)



