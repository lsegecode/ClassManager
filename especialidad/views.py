from django.shortcuts import render, redirect
from .models import Especialidad
from .forms import EspecialidadForm, EspecialidadFormUpdate

# Create your views here.
def especialidad(request):
    especialidad_form = EspecialidadForm()
    especialidad = Especialidad.objects.all()


    if request.method == 'POST':
        especialidad_form = EspecialidadForm(data=request.POST)

        if especialidad_form.is_valid():
            especialidad_form.save()
            return redirect('/especialidad')

    context = {
        'especialidad_form' :especialidad_form,
        'especialidad': especialidad
    }
    return render(request, 'gestion_especialidad.html', context)

def verEspecialidad(request, id_especialidad):
    especialidad = Especialidad.objects.get(id_especialidad=id_especialidad)
    return render(request, "verEspecialidad.html", {"especialidad":especialidad})

def editarEspecialidad(request, id_especialidad):
    queryset = Especialidad.objects.get(id_especialidad=id_especialidad)
    especialidad_form_update = EspecialidadFormUpdate(instance=queryset)
    if request.method == 'POST':
        especialidad_form_update = EspecialidadFormUpdate(request.POST, instance=queryset)
        if especialidad_form_update.is_valid():
            especialidad_form_update.save()
            return redirect('/especialidad')
    
    context = {
		'especialidad_form_update':especialidad_form_update,
	}
    return render(request, 'editarEspecialidad.html', context)


def eliminarEspecialidad(request, id_especialidad):
    especialidad = Especialidad.objects.get(id_especialidad=id_especialidad)
    especialidad.delete()

    return redirect('/especialidad')