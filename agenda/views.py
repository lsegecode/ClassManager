from django.shortcuts import render, redirect
from .models import Agenda
from .forms import AgendaForm, AgendaFormUpdate

# Create your views here.
def agenda(request):
    agenda_form = AgendaForm()
    agenda = Agenda.objects.all()


    if request.method == 'POST':
        agenda_form = AgendaForm(data=request.POST)

        if agenda_form.is_valid():
            agenda_form.save()
            return redirect('/agenda')
    
    context = {
        'agenda_form':agenda_form, 
        'agenda':agenda
    }

    return render(request, 'gestion_agenda.html', context)

def verAgenda(request, id_agenda):
    agenda = Agenda.objects.get(id_agenda=id_agenda)
    return render(request, "verAgenda.html", {"agenda":agenda})

def editarAgenda(request, id_agenda):
    queryset = Agenda.objects.get(id_agenda=id_agenda)
    agenda_form_update = AgendaFormUpdate(instance=queryset)
    if request.method == 'POST':
        agenda_form_update = AgendaFormUpdate(request.POST, instance=queryset)
        if agenda_form_update.is_valid():
            agenda_form_update.save()
            return redirect('/agenda')
    
    context = {
		'agenda_form_update':agenda_form_update,
	}
    return render(request, 'editarAgenda.html', context)

def eliminarAgenda(request, id_agenda):
    agenda = Agenda.objects.get(id_agenda=id_agenda)
    agenda.delete()

    return redirect('/agenda')