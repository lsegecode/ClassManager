from django.shortcuts import render, redirect
from .models import Notas
from .forms import NotasForm, NotasFormUpdate

# Create your views here.
def notas(request):
    notas_form = NotasForm()
    notas = Notas.objects.all()


    if request.method == 'POST':
        notas_form = NotasForm(data=request.POST)

        if notas_form.is_valid():
            notas_form.save()
            return redirect('/notas')
    
    context = {
        'notas_form' :notas_form,
        'notas': notas
    }
    return render(request, 'gestion_notas.html', context)

def verNota(request, id_nota):
    notas = Notas.objects.get(id_nota=id_nota)
    return render(request, "verNotas.html", {"notas":notas})

def editarNota(request, id_nota):
    queryset = Notas.objects.get(id_nota=id_nota)
    Enota_form = NotasFormUpdate(instance=queryset)
    if request.method == 'POST':
        Enota_form = NotasFormUpdate(request.POST, instance=queryset)
        if Enota_form.is_valid():
            Enota_form.save()
            return redirect('/notas')
    
    context = {
		'Enota_form':Enota_form,
	}
    return render(request, 'editarNotas.html', context)

def eliminarNota(request, id_nota):
    notas = Notas.objects.get(id_nota=id_nota)
    notas.delete()

    return redirect('/notas')