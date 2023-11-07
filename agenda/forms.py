from django import forms
from .models import Agenda


class AgendaForm(forms.ModelForm):

    class Meta:
        model = Agenda
        fields = ['id_agenda', 'descripcion', 'id_personal']


class AgendaFormUpdate(forms.ModelForm):

    class Meta:
        model = Agenda
        fields = ['id_agenda', 'descripcion', 'id_personal']
