from django.shortcuts import render, redirect
from .models import Asistencia
from .forms import AsistenciaForm, AsistenciaFormUpdate

# Create your views here.
def asistencia(request):
    asistencia_form = AsistenciaForm()
    asistencia = Asistencia.objects.all()


    if request.method == 'POST':
        asistencia_form = AsistenciaForm(data=request.POST)

        if asistencia_form.is_valid():
            asistencia_form.save()
            return redirect('/asistencia')

    return render(request, 'gestion_asistencia.html', {'asistencia_form':asistencia_form, 'asistencia':asistencia})

def verAsistencia(request, id_asistencia):
    asistencia = Asistencia.objects.get(id_asistencia=id_asistencia)
    return render(request, "verAsistencia.html", {"asistencia":asistencia})

def editarAsistencia(request, id_asistencia):
    queryset = Asistencia.objects.get(id_asistencia=id_asistencia)
    Easistencia_form = AsistenciaFormUpdate(instance=queryset)
    if request.method == 'POST':
        Easistencia_form = AsistenciaFormUpdate(request.POST, instance=queryset)
        if Easistencia_form.is_valid():
            Easistencia_form.save()
            return redirect('/asistencia')
    
    context = {
		'Easistencia_form':Easistencia_form,
	}
    return render(request, 'editarAsistencia.html', context)

def eliminarAsistencia(request, id_asistencia):
    asistencia = Asistencia.objects.get(id_asistencia=id_asistencia)
    asistencia.delete()

    return redirect('/asistencia')