from django.http import request
from django.shortcuts import render,redirect
from .models import Tatuador,Diseno
from .form import TatuadorForm,DisenoForm


# Create your views here.
def index(request):
    tatuadores = Tatuador.objects.all()
    print(tatuadores)
    datos = {
        'tatuadores':tatuadores
    }
    return render(request,'app/Index.html',datos)
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
        formulario = TatuadorForm(request.POST or None,request.FILES or None)

        if formulario.is_valid:
            image=formulario.save()
            print(image.imagen.url)
            formulario.save()
            data["mensaje"]="Guardado correctamente"
      

    return render(request,'app/form_tatuador.html',data)

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
    return render(request,'app/form_tatuador.html',data)


def form_del_tatuador(request,id):
    tatuador=Tatuador.objects.get(idTatuador=id)
    tatuador.delete()
    return redirect(to="test")

#-----------

def testt(request):
    disenos = Diseno.objects.all()
    datoss = {
        'disenos':disenos
    }
    return render(request,'core/testt.html',datoss)


def form_diseno(request):
    dataa={
        'formm': DisenoForm()
    }
    if request.method=='POST':
        formularioo = DisenoForm(request.POST or None,request.FILES or None)
        if formularioo.is_valid:
            formularioo.save()
            dataa["mensajee"]="Subido correctamente"


    return render(request,'app/form_diseno.html',dataa)

def form_mod_diseno(request,id):
    diseno = Diseno.objects.get(idDiseno=id)
    dataa={
        'formm':DisenoForm(instance=diseno)
    }
    if request.method == 'POST':
        formularioo=DisenoForm(dataa=request.POST,instance=diseno)

        if formularioo.is_valid:
            formularioo.save()
            dataa["mensajee"]="modificado correctamente"
    return render(request,'app/form_diseno.html',dataa)
    
    

def form_del_diseno(request,id):
    diseno=Diseno.objects.get(idDiseno=id)
    diseno.delete()
    return redirect(to="testt")

