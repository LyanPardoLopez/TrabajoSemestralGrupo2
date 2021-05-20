from django.urls import path
from .views import index
from .views import formulario,Login,Register
from .views import perfilKV,perfilML,perfilMP,perfilMR



urlpatterns =[
    path('',index,name="index"),
    path('formulario',formulario,name="formulario"),
    path('Login',Login,name="Login"),
    path('Register',Register,name="Register"),
    path('perfilKV',perfilKV,name="perfilKV"),
    path('perfilML',perfilML,name="perfilML"),
    path('perfilMP',perfilMP,name="perfilMP"),
    path('perfilMR',perfilMR,name="perfilMR"),
]