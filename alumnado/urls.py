from django.urls import path
from . import views

app_name = 'alumnos'

urlpatterns = [
    path('', views.alumnos, name='alumnos'),
    path('verAlumno/<id_alumno>', views.verAlumno, name='ver_alumno'),
    path('editarAlumno/<id_alumno>/', views.editarAlumno, name='editar_alumno'),
    path('eliminarAlumno/<id_alumno>/', views.eliminarAlumno, name='eliminar_alumno'),
]
