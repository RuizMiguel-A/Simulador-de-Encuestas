# Encuestas/forms.py
from django import forms
from .models import Encuesta, Pregunta, Opcion

class EncuestaForm(forms.ModelForm):
    class Meta:
        model = Encuesta
        fields = ['titulo', 'descripcion']

class PreguntaForm(forms.ModelForm):
    class Meta:
        model = Pregunta
        # Se ha corregido el nombre del campo de 'texto_pregunta' a 'texto'.
        fields = ['texto']

class OpcionForm(forms.ModelForm):
    class Meta:
        model = Opcion
        fields = ['texto']
