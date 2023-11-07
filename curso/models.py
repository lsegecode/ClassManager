from django.db import models
from materia import models as materias_models


# Create your models here.
class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    Annio = models.CharField(max_length=5)
    Division = models.CharField(max_length=4)
    id_materia = models.ForeignKey(materias_models.Materia, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        texto = "{0}, {1}"
        return texto.format(self.Annio, self.Division)