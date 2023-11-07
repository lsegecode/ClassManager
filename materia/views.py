from django.shortcuts import render, redirect
from .models import Materia
from .forms import MateriaForm, MateriaFormUpdate
# Create your views here.

def materia(request):
    materia_form = MateriaForm()
    materia = Materia.objects.all()

    if request.method == 'POST':
        materia_form = MateriaForm(data=request.POST)

        if materia_form.is_valid():
            materia_form.save()
            return redirect('/materias')

    return render(request, 'gestion_materia.html', {'materia_form':materia_form, 'materia':materia})

def verMateria(request, id_materia):
    materia = Materia.objects.get(id_materia=id_materia)
    return render(request, "verMateria.html", {"materia":materia})

def editarMateria(request, id_materia):
    queryset = Materia.objects.get(id_materia=id_materia)
    materia_form_update = MateriaFormUpdate(instance=queryset)
    if request.method == 'POST':
        materia_form_update = MateriaFormUpdate(request.POST, instance=queryset)
        if materia_form_update.is_valid():
            materia_form_update.save()
            return redirect('/materias')
    
    context = {
		'materia_form_update':materia_form_update,
	}
    return render(request, 'editarMateria.html', context)

def eliminarMateria(request, c):
    materia = Materia.objects.get(id_materia=id_materia)
    materia.delete()

    return redirect('/materias')