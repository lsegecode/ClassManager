from django.shortcuts import render, redirect
from .models import Alumno
from django.contrib import messages


def index(request):
    return render(request, "index.html")

def alumnos(request):
    alumnos = Alumno.objects.all()

    return render(request, "gestion_alumnos.html", {"alumnos": alumnos})

def registrarAlumno(request):
    dni_a=request.POST['dni_a']
    cuil_a=request.POST['cuil_a']
    apellido_a=request.POST['apellido_a']
    nombre_a=request.POST['nombre_a']
    matricula=request.POST['matricula']
    tutores=request.POST['tutores']
    telefono=request.POST['telefono']
    direccion=request.POST['direccion']
    fecha_nac=request.POST['fecha_nac']

    alumno = Alumno.objects.create(
        dni_a=dni_a, 
        cuil_a=cuil_a, 
        apellido_a=apellido_a,
        nombre_a=nombre_a,
        matricula=matricula,
        tutores=tutores,
        telefono=telefono,
        direccion=direccion,
        fecha_nac=fecha_nac
        )
    messages.success(request, '¡Curso registrado!')
    return redirect('/alumnos')

def verAlumno(request, id_alumno):
    alumno = Alumno.objects.get(id_alumno=id_alumno)
    return render(request, "verAlumno.html", {"alumno": alumno})

def edicionAlumno(request, id_alumno):
    alumno = Alumno.objects.get(id_alumno=id_alumno)
    return render(request, "edicionAlumno.html", {"alumno": alumno})

def editarAlumno(request):
    id_alumno=request.POST['id_alumno']
    dni_a=request.POST['dni_a']
    cuil_a=request.POST['cuil_a']
    apellido_a=request.POST['apellido_a']
    nombre_a=request.POST['nombre_a']
    matricula=request.POST['matricula']
    tutores=request.POST['tutores']
    telefono=request.POST['telefono']
    direccion=request.POST['direccion']
    fecha_nac=request.POST['fecha_nac']

    alumno = Alumno.objects.get(id_alumno=id_alumno)
    alumno.dni_a= dni_a
    alumno.cuil_a = cuil_a
    alumno.apellido_a = apellido_a
    alumno.nombre_a = nombre_a
    alumno.matricula = matricula
    alumno.tutores = tutores
    alumno.telefono = telefono
    alumno.direccion = direccion
    alumno.fecha_nac = fecha_nac
    alumno.save()

    messages.success(request, '¡Curso actualizado!')

    return redirect('/alumnos')
    

def eliminarAlumno(request, id_alumno):
    alumno = Alumno.objects.get(id_alumno=id_alumno)
    alumno.delete()

    return redirect('/alumnos')
