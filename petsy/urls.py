from django.contrib import admin
from unicodedata import name
from django.urls import path 
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('calculadora', calculadora, name="calculadora"),
    path('Contacto', Contacto, name="Contacto"),
    path('Feriados', Feriados, name="Feriados"),
    path('galeria', galeria, name="galeria"),
    path('registracion', registracion, name="registracion"),
    path('somos', somos, name="somos"),
    path('mostrar/', mostrar, name="mostrar"),
    path('form_accesorio/', form_accesorio, name="form_accesorio"), 
    path('form_modaccesorio/<id>', form_modaccesorio, name="form_modaccesorio"),
    path('form_del_accesorio/<id>', form_del_accesorio, name="form_del_accesorio"),
    path('MostrarCliente/', MostrarCliente, name="MostrarCliente"),
    path('CrearCliente/', CrearCliente, name="CrearCliente"),
    path('form_modcliente/<id>', form_modcliente, name="form_modcliente"),
    path('EliminarCliente/<id>', EliminarCliente, name="EliminarCliente"),


]