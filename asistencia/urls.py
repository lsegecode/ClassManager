from django.urls import path
from . import views

app_name = 'asistencia'

urlpatterns = [
    path('', views.asistencia, name='asistencia'),
    #path('verAsistencia/<id_asistencia>', views.verAsistencia, name='ver_asistencia'),
    #path('edicionAsistencia/<id_asistencia>/', views.edicionAsistencia, name='edicion_asistencia'),
    #path('editarAsistencia/', views.editarAsistencia, name='editar_asistencia'),
    #path('eliminarAsistencia/<id_asistencia>/', views.eliminarAsistencia, name='eliminar_asistencia'),
]