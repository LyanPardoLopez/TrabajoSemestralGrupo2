from django.urls import path
from .views import index
from .views import formulario,Login,Register
from .views import test,form_tatuador,form_mod_tatuador,form_del_tatuador
from .views import testt,form_diseno,form_del_diseno,form_mod_diseno
from .views import perfilKV,perfilML,perfilMP,perfilMR
from .views import apitest



urlpatterns =[
    path('',index,name="index"),


    path('test',test,name='test'),

    path('form_tatuador',form_tatuador,name='form_tatuador'),

    path('form_mod_tatuador/<id>',form_mod_tatuador,name='form_mod_tatuador'),

    path('form_del_tatuador/<id>',form_del_tatuador,name='form_del_tatuador'),



    path('testt',testt,name='testt'),

    path('form_diseno',form_diseno,name='form_diseno'),

    path('form_mod_diseno/<id>',form_mod_diseno,name='form_mod_diseno'),

    path('form_del_diseno/<id>',form_del_diseno,name='form_del_diseno'),




    path('formulario',formulario,name="formulario"),

    path('Login',Login,name="Login"),

    path('Register',Register,name="Register"),

    path('perfilKV',perfilKV,name="perfilKV"),

    path('perfilML',perfilML,name="perfilML"),

    path('perfilMP',perfilMP,name="perfilMP"),

    path('perfilMR',perfilMR,name="perfilMR"),




    path('apitest',apitest,name='apitest'),


]
