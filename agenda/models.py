from django.db import models
from personal import models as personal_models

# Create your models here.

class Agenda(models.Model):
    id_agenda = models.AutoField(primary_key=True)
    fecha_hora = models.DateTimeField(auto_now_add=True,verbose_name='Hora')
    descripcion = models.TextField()
    id_personal = models.ForeignKey(personal_models.Personal, on_delete=models.CASCADE, default=0)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.id_personal)