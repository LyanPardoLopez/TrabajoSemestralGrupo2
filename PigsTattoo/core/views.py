from django.http import request
from django.shortcuts import render,redirect
from .models import Tatuador
from .form import TatuadorForm


# Create your views here.
def index(request):
    return render(request,'core/Index.html')
def formulario(request):
    return render(request,'core/formulario.html')
def Login(request):
    return render(request,'core/Login.html')
def Register(request):
    return render(request,'core/Register.html')
def perfilKV(request):
    return render(request,'core/PerfilKatVonD.html')
def perfilML(request):
    return render(request,'core/PerfilMariaLeon.html')
def perfilMP(request):
    return render(request,'core/PerfilMauricioPartida.html')
def perfilMR(request):
    return render(request,'core/PerfilMikeRubendall.html')


def test(request):
    tatuadores = Tatuador.objects.all()
    datos = {
        'tatuadores':tatuadores
    }
    return render(request,'core/test.html',datos)


def form_tatuador(request):

    data={
        'form': TatuadorForm()
    }
    if request.method=='POST':
        formulario = TatuadorForm(request.POST)

        if formulario.is_valid:
            formulario.save()
            data["mensaje"]="Guardado correctamente"
      

    return render(request,'core/form_tatuador.html',data)

def form_mod_tatuador(request,id):
    tatuador = Tatuador.objects.get(idTatuador=id)
    data={
        'form':TatuadorForm(instance=tatuador)
    }
    if request.method =='POST':
        formulario=TatuadorForm(data=request.POST,instance=tatuador)

        if formulario.is_valid:
            formulario.save()
            data['mensaje']="Modifacados correctamente"
        return render(request,'core/form_tatuador.html',data)

def form_del_tatuador(request,id):
    tatuador=Tatuador.objects.get(idTatuador=id)
    tatuador.delete()
    return redirect(to="test")