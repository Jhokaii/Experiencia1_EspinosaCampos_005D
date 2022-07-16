from cProfile import label
from dataclasses import fields
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import  Planta, Cliente, Categoria



class   PlantaForms(forms.ModelForm):
    class Meta:
        model = Planta
        fields = ['nombre', 'color']
        labels ={
            'nombre' : 'Nombre',
            'color' : 'Color',
    
        }

        widgets = {
            'nombre': forms.TextInput(
                attrs={
                'class': 'form-control',
                'placeholder' : 'Ingrese nombre de la planta',
                'id' : 'nombre'
                }
            ),

            'color': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el color de la planta',
                    'id' : 'color'
                }
            )

        }

class ClienteForm(ModelForm):


    class Meta:
        model = Cliente
        fields =['rut','nombre','gmail','telefono','direccion']
        labels ={
            'rut': 'Rut', 
            'nombre': 'Nombre', 
            'gmail': 'Gmail', 
            'telefono': 'Telefono',
            'direccion': 'Direccion',
        }
        widgets={
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese rut', 
                    'id': 'rut'
                }
            ), 
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese nombre', 
                    'id': 'nombre'
                }
            ), 
            'gmail': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese gmail', 
                    'id': 'gmail'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese telefono', 
                    'id': 'telefono'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese direccion', 
                    'id': 'direccion'
                }
            ),

        }