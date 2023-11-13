from django.forms import ModelForm
from .models import paciente
from django import forms

class PacienteForm(ModelForm):
    class Meta:
        model= paciente
        fields=['DNI','nombre','edad','genero']


class FiltroFechaForm(forms.Form):
    fecha_inicio = forms.DateField(
        label='Fecha de inicio',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'custom-date-input'}),
        required=False
    )
    fecha_fin = forms.DateField(
        label='Fecha de fin',
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'custom-date-input'}),
        required=False
    )