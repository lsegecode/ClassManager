from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import AsistenciaForm
from .models import Asistencia

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
