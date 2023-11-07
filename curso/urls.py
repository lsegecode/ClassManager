from django.urls import path
from . import views

app_name = 'curso'

urlpatterns = [
    path('', views.curso, name='curso'),
    path('verCurso/<id_curso>', views.verCurso, name='ver_curso'),
    path('editarCurso/<id_curso>/', views.editarCurso, name='editar_curso'),
    path('eliminarCurso/<id_curso>/', views.eliminarCurso, name='eliminar_curso'),
]