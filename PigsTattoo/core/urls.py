from django.urls import path
from .views import index
from .views import formulario,Login,Register
from .views import test,form_tatuador,form_mod_tatuador,form_del_tatuador
from .views import testt,form_diseño,form_del_diseño,form_mod_diseño
from .views import perfilKV,perfilML,perfilMP,perfilMR



urlpatterns =[
    path('',index,name="index"),


    path('test',test,name='test'),

    path('form_tatuador',form_tatuador,name='form_tatuador'),

    path('form_mod_tatuador/<id>',form_mod_tatuador,name='form_mod_tatuador'),

    path('form_del_tatuador/<id>',form_del_tatuador,name='form_del_tatuador'),

    path('testt',testt,name='testt'),

    path('form_diseño',form_diseño,name='form_diseño'),

    path('form_mod_diseño/<id>',form_mod_diseño,name='form_mod_diseño'),

    path('form_del_diseño/<id>',form_del_diseño,name='form_del_diseño'),


    path('formulario',formulario,name="formulario"),

    path('Login',Login,name="Login"),

    path('Register',Register,name="Register"),

    path('perfilKV',perfilKV,name="perfilKV"),

    path('perfilML',perfilML,name="perfilML"),

    path('perfilMP',perfilMP,name="perfilMP"),

    path('perfilMR',perfilMR,name="perfilMR"),


]
