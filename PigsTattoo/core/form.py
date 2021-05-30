from django import forms
from django.forms import ModelForm
from .models import Tatuador,Diseño

class TatuadorForm(ModelForm):

    class Meta:
        model = Tatuador
        #filds = ['idTatuador','nombreTatuador','estiloTataudor']
        fields = '__all__'


class DiseñoForm(ModelForm):
    class Meta:
        model = Diseño
        fields='__all__'