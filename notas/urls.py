from django.urls import path
from . import views

app_name = 'notas'

urlpatterns = [
    path('', views.notas, name='notas'),
    path('verNota/<id_nota>', views.verNota, name='ver_nota'),
    path('editarNota/<id_nota>/', views.editarNota, name='editar_nota'),
    path('eliminarNota/<id_nota>/', views.eliminarNota, name='eliminar_nota'),
]