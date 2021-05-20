from django.shortcuts import render

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

