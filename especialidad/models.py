from django.db import models

# Create your models here.
class Especialidad(models.Model):
    id_especialidad = models.AutoField(primary_key=True)
    nombreEspecialidad=models.CharField(max_length=50)
    disenioCurricular=models.CharField(max_length=20)
    cantidadMaterias=models.CharField(max_length=3)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombreEspecialidad)