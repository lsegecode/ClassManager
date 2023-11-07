from django.urls import path
from . import views

app_name = 'personal'

urlpatterns = [
    path('', views.personal, name='personal'),
    path('verPersonal/<id_personal>', views.verPersonal, name='ver_personal'),
    path('editarPersonal/<id_personal>/', views.editarPersonal, name='editar_personal'),
    path('eliminarPersonal/<id_personal>/', views.eliminarPersonal, name='eliminar_personal'),
]

