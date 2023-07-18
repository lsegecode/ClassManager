from django.urls import path
from . import views

urlpatterns = [
    path('alumnos', views.home),
    path('', views.index),

]