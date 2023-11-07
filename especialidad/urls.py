from django.urls import path
from . import views

app_name = 'especialidad'

urlpatterns = [
    path('', views.especialidad, name='especialidad'),
    path('verEspecialidad/<id_especialidad>', views.verEspecialidad, name='ver_especialidad'),
    path('editarEspecialidad/<id_especialidad>/', views.editarEspecialidad, name='editar_especialidad'),
    path('eliminarEspecialidad/<id_especialidad>/', views.eliminarEspecialidad, name='eliminar_especialidad'),
]