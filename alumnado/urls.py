from django.urls import path
from . import views

app_name = 'alumnos'

urlpatterns = [
    path('', views.alumnos, name='alumnos'),
    path('registrarAlumno/', views.registrarAlumno, name='registrar_alumno'),
    path('verAlumno/<id_alumno>', views.verAlumno, name='ver_alumno'),
    path('edicionAlumno/<id_alumno>/', views.edicionAlumno, name='edicion_alumno'),
    path('editarAlumno/', views.editarAlumno, name='editar_alumno'),
    path('eliminarAlumno/<id_alumno>/', views.eliminarAlumno, name='eliminar_alumno'),
]
