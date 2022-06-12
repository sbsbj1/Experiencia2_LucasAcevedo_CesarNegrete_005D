from cProfile import label
from dataclasses import field, fields
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget

from petsy.models import Accesorio, Categoria
from petsy.models import Cliente

class AccesorioForm(forms.ModelForm):

    class Meta:
        model = Accesorio
        fields = ['idProducto', 'clase', 'stock', 'categoria', 'imagen']
        labels = {
            'idProducto': 'IDProducto',
            'clase': 'Clase',
            'stock': 'Stock',
            'categoria': 'Categoria',
            'imagen': 'Imagen'
        }
        widgets={
            'idProducto': forms.TextInput(
                attrs={     
                    'class': 'form-control',
                    'placeholder': 'Ingrese ID del Producto',
                    'id': 'ID'
                }
            ),
            'clase': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la clase del Producto',
                    'id': 'clase'
                }
            ),
            'stock': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el stock del Producto',
                    'id': 'stock'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria'
                }
            ),
            'imagen': forms.ClearableFileInput(
                attrs={
                  'class': 'form-control',
                    'id': 'imagen'  
                }
            )
        }



#Cliente Form
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['Rut_Cliente', 'Nombre', 'Transaciones']
        labels = {
            'Rut_Cliente': 'rut_cliente',
            'Nombre': 'nombre',
            'Transaciones': 'transaciones',
        }
        widgets={
            'Rut_Cliente': forms.TextInput(
                attrs={     
                    'class': 'form-control',
                    'placeholder': 'Ingrese Rut Del Cliente',
                    'id': 'Rut_Cliente'
                }
            ),
            'Nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre Del Cliente',
                    'id': 'Nombre'
                }
            ),
            'Transaciones': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el Numero De Transaciones',
                    'id': 'Transaciones'
                }
            )
        }