from django import forms
from django.forms import ModelForm
from .models import Tatuador

class TatuadorForm(ModelForm):

    class Meta:
        model = Tatuador
        fields = '__all__'
        