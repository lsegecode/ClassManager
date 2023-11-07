from django.shortcuts import render, redirect
from .models import Curso
from .forms import CursoForm, CursoFormUpdate

# Create your views here.
def curso(request):
    curso_form = CursoForm()
    curso = Curso.objects.all()

    if request.method == 'POST':
        curso_form = CursoForm(data=request.POST)

        if curso_form.is_valid():
            curso_form.save()
            return redirect('/curso')
    
    context = {
        'curso' : curso,
        'curso_form' : curso_form
    }
    return render(request, 'gestion_curso.html', context)

def verCurso(request, id_curso):
    curso = Curso.objects.get(id_curso=id_curso)
    return render(request, "verCurso.html", {"curso":curso})

def editarCurso(request, id_curso):
    queryset = Curso.objects.get(id_curso=id_curso)
    Ecurso_form = CursoFormUpdate(instance=queryset)
    if request.method == 'POST':
        Ecurso_form = CursoFormUpdate(request.POST, instance=queryset)
        if Ecurso_form.is_valid():
            Ecurso_form.save()
            return redirect('/curso')
    
    context = {
		'Ecurso_form':Ecurso_form,
	}
    return render(request, 'editarCurso.html', context)

def eliminarCurso(request, id_curso):
    curso = Curso.objects.get(id_curso=id_curso)
    curso.delete()

    return redirect('/curso')