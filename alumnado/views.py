from django.shortcuts import render, redirect
from .models import Alumno
from .forms import AlumnoForm, AlumnoFormUpdate

def alumnos(request):
    alumnos_form = AlumnoForm()
    alumnos = Alumno.objects.all()
    
    if request.method == 'POST':
        alumnos_form = AlumnoForm(data=request.POST)
        
        if alumnos_form.is_valid():
            alumnos_form.save()
            return redirect('/alumnos')
    
    context = {
        'alumnos_form' : alumnos_form,
        'alumnos' : alumnos
    }
    return render(request, 'gestion_alumnos.html', context)

def verAlumno(request, id_alumno):
    alumno = Alumno.objects.get(id_alumno=id_alumno)
    return render(request, "verAlumno.html", {"alumno": alumno})

def editarAlumno(request, id_alumno):
    queryset = Alumno.objects.get(id_alumno=id_alumno)
    alumno_form_update = AlumnoFormUpdate(instance=queryset)
    if request.method == 'POST':
        alumno_form_update = AlumnoFormUpdate(request.POST, instance=queryset)
        if alumno_form_update.is_valid():
            alumno_form_update.save()
            return redirect('/alumnos')
    
    context = {
		'alumno_form_update':alumno_form_update,
	}
    return render(request, 'edicionAlumno.html', context)
    
def eliminarAlumno(request, id_alumno):
    alumno = Alumno.objects.get(id_alumno=id_alumno)
    alumno.delete()
    return redirect('/alumnos')

