from django.shortcuts import render, redirect
from .models import Personal
from .forms import PersonalForm, PersonalFormUpdate

# Create your views here.
def personal(request):
    personal_form = PersonalForm()
    personal = Personal.objects.all()


    if request.method == 'POST':
        personal_form = PersonalForm(data=request.POST)

        if personal_form.is_valid():
            personal_form.save()
            return redirect('/personal')
    context = {
        'personal_form' :personal_form,
        'personal': personal
    }
    
    return render(request, 'gestion_personal.html', context)

def verPersonal(request, id_personal):
    personal = Personal.objects.get(id_personal=id_personal)
    return render(request, "verPersonal.html", {"personal": personal})  

def editarPersonal(request, id_personal):
    queryset = Personal.objects.get(id_personal=id_personal)
    personal_form_update = PersonalFormUpdate(instance=queryset)
    if request.method == 'POST':
        personal_form_update = PersonalFormUpdate(request.POST, instance=queryset)
        if personal_form_update.is_valid():
            personal_form_update.save()
            return redirect('/personal')
    
    context = {
		'personal_form_update':personal_form_update,
	}
    return render(request, 'edicionPersonal.html', context)

def eliminarPersonal(request, id_personal):
    personal = Personal.objects.get(id_personal=id_personal)
    personal.delete()

    return redirect('/personal')