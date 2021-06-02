from django import forms
from django.forms import ModelForm
from .models import Tatuador,Diseno

class TatuadorForm(ModelForm):

    class Meta:
        model = Tatuador
        #filds = ['idTatuador','nombreTatuador','estiloTataudor']
        fields = '__all__'


class DisenoForm(ModelForm):
    class Meta:
        model = Diseno
        fields='__all__'