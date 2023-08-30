from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('alumnos/', views.alumnos),
    path('registrarAlumno/', views.registrarAlumno),
    path('verAlumno/<id_alumno>', views.verAlumno),
    path('edicionAlumno/<id_alumno>/', views.edicionAlumno),
    path('editarAlumno/', views.editarAlumno),
    path('eliminarAlumno/<id_alumno>/', views.eliminarAlumno)
]
