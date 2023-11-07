from django.urls import path
from . import views

app_name = 'materia'

urlpatterns = [
    path('', views.materia, name='materia'),
    path('verMateria/<id_materia>', views.verMateria, name='ver_materia'),
    path('editarMateria/<id_materia>/', views.editarMateria, name='editar_materia'),
    path('eliminarMateria/<id_materia>/', views.eliminarMateria, name='eliminar_materia'),
]