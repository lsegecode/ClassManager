from django.urls import path
from . import views

app_name = 'profesores'

urlpatterns = [
    path('', views.profesor, name='profesores'),
    path('registrarProfesor/', views.registrarProfesor, name='registrar_profesor'),
    path('verProfesor/<id_profesor>', views.verProfesor, name='ver_profesor'),
    path('edicionProfesor/<id_profesor>/', views.edicionProfesor, name='edicion_profesor'),
    path('editarProfesor/', views.editarProfesor, name='editar_profesor'),
    path('eliminarProfesor/<id_profesor>/', views.eliminarProfesor, name='eliminar_profesor'),
]