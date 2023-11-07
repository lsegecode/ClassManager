from django.db import models
from materia import models as materias_models
from alumnado import models as alumnos_models

# Create your models here.
class Notas(models.Model):
    id_nota = models.AutoField(primary_key=True)
    valor = models.CharField(max_length=3)
    AnnioCursada = models.CharField(max_length=5)
    instancia = models.CharField(max_length=30)
    fechaNota = models.DateField()
    id_alumno = models.ForeignKey(alumnos_models.Alumno, on_delete=models.CASCADE)
    id_materia = models.ForeignKey(materias_models.Materia, on_delete=models.CASCADE)
    

    def __str__(self):
        texto = "{0}"
        return texto.format(self.valor)