from django.urls import path
from rest_tatuador.views import lista_tatuadores
from .views import detalle_tatuador
from .viewsLogin import login
urlpatterns=[
    path('lista_tatuadores',lista_tatuadores,name="lista_tatuadores"),
    path('detalle_tatuador/<id>',detalle_tatuador,name="detalle_tatuador"),
    path('login',login,name="login"),
]