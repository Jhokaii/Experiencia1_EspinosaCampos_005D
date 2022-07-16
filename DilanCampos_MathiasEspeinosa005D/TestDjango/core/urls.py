from django.urls import path
from unicodedata import name
from .views import *
from django.contrib import admin


urlpatterns = [
    path('', index, name = "index"),
    path('contacto/', contacto,  name = "contacto" ),
    path('galeria/', galeria, name = "galeria" ),
    path('registro/', registro, name = "registro"),
    path('somos/', somos, name = "somos"),
    path('mostrar/', mostrar, name= "mostrar"),
    path('form_planta/<id>', form_planta, name = "form_planta"),
    path('form_modplanta/<id>', form_modplanta, name= "form_modplanta"),
    path('form_de_planta/<id>', form_de_planta, name= "form_de_planta"),
    path('clientes/', clientes, name="form_cliente"),
    path('form_modcliente/<id>', form_modcliente, name="form_modcliente"),
    path('form_del_cliente/<id>', form_del_cliente, name="form_del_cliente"),
]