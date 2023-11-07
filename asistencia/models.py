from django.db import models
from alumnado import models as alumnado_models

options = [
    [0, 'Regular'],
    [1, 'Semipresencial'],
    [2, 'Libre'],
]
# Create your models here.
class Asistencia(models.Model):
    id_asistencia = models.AutoField(primary_key=True)
    fechaA = models.DateField(verbose_name='Fecha')
    horaA = models.DateTimeField(auto_now_add=True,verbose_name='Hora')
    condicion = models.IntegerField(choices=options, verbose_name='Condición')
    cantidadA = models.CharField(max_length=3, blank=True, verbose_name='Cantidad de Inasistencias')
    turno = models.CharField(max_length=30, blank=True, verbose_name='Turno')
    reintegrado = models.BooleanField(default=False, verbose_name='Reintegrado')
    id_alumno = models.ForeignKey(alumnado_models.Alumno, on_delete=models.CASCADE, default=0)
    evento = models.CharField(max_length=30, blank=True)

    def __str__(self):
        texto = "{0} {1}"
        return texto.format(self.id_alumno, self.id_asistencia)
    