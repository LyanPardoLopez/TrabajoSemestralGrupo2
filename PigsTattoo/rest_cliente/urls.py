from django.urls import path
from rest_cliente.views import lista_registro
from .views import detalle_registro
from .viewsLogin import login
urlpatterns=[
    path('lista_registro',lista_registro,name="lista_registro"),
    path('detalle_registro/<id>',detalle_registro,name="detalle_registro"),
    path('login',login,name="login"),
]