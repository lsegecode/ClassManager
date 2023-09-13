from django.shortcuts import render, redirect
from .models import Profesor
from django.contrib import messages

def profesor(request):
    profesores = Profesor.objects.all()

    return render(request, "gestion_profesor.html", {"profesores": profesores})

def registrarProfesor(request):
    dni_p=request.POST['dni_p']
    cuil_p=request.POST['cuil_p']
    apellido_p=request.POST['apellido_p']
    nombre_p=request.POST['nombre_p']
    legajo_p=request.POST['legajo_p']
    telefono_p=request.POST['telefono_p']
    direccion_p=request.POST['direccion_p']
    fecha_nac_p=request.POST['fecha_nac_p']

    profesor = Profesor.objects.create(
        dni_p=dni_p, 
        cuil_p=cuil_p, 
        apellido_p=apellido_p,
        nombre_p=nombre_p,
        legajo_p=legajo_p,
        telefono_p=telefono_p,
        direccion_p=direccion_p,
        fecha_nac_p=fecha_nac_p,
        )
    messages.success(request, '¡Profesor Registrado!')
    return redirect('/profesores')

def verProfesor(request, id_profesor):
    profesor = Profesor.objects.get(id_profesor=id_profesor)
    return render(request, "verProfesor.html", {"profesor": profesor})

def edicionProfesor(request, id_profesor):
    profesor = Profesor.objects.get(id_profesor=id_profesor)
    return render(request, "edicionProfesor.html", {"profesor": profesor})

def editarProfesor(request):
    id_profesor=request.POST['id_profesor']
    dni_p=request.POST['dni_p']
    cuil_p=request.POST['cuil_p']
    apellido_p=request.POST['apellido_p']
    nombre_p=request.POST['nombre_p']
    legajo_p=request.POST['legajo_p']
    telefono_p=request.POST['telefono_p']
    direccion_p=request.POST['direccion_p']
    fecha_nac_p=request.POST['fecha_nac_p']

    profesor = Profesor.objects.get(id_profesor=id_profesor)
    profesor.dni_p= dni_p
    profesor.cuil_p = cuil_p
    profesor.apellido_p = apellido_p
    profesor.nombre_p = nombre_p
    profesor.legajo_p = legajo_p
    profesor.telefono_p = telefono_p
    profesor.direccion_p = direccion_p
    profesor.fecha_nac_p = fecha_nac_p
    profesor.save()

    messages.success(request, '¡Profesor actualizado!')

    return redirect('/profesores')
    
def eliminarProfesor(request, id_profesor):
    profesor = Profesor.objects.get(id_profesor=id_profesor)
    profesor.delete()

    return redirect('/profesores')
