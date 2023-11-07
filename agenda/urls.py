from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.agenda, name='agenda'),
    path('verAgenda/<id_agenda>', views.verAgenda, name='ver_agenda'),
    path('editarAgenda/<id_agenda>/', views.editarAgenda, name='editar_agenda'),
    path('eliminarAgenda/<id_agenda>/', views.eliminarAgenda, name='eliminar_agenda'),
]