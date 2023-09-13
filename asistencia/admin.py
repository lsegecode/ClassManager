from django.contrib import admin
from .models import Asistencia

# Register your models here.
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('id_alumno', 'fechaA', 'horaA', 'condicion', 'cantidadA', 'turno')
    list_filter = ('id_alumno', 'fechaA')

admin.site.register(Asistencia, AsistenciaAdmin)