from pyexpat import model
from django.db import models
from tabnanny import verbose
from cgi import print_arguments
from contextlib import nullcontext

# Create your models here.

class Categoria (models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la categoria')
    

    def __str__(self):
        return self.nombreCategoria

class Planta (models.Model):
    nombre = models.CharField(max_length=50, primary_key=True, verbose_name='Nombre')
    color = models.CharField(max_length=50, verbose_name='Color de la planta')

    

    def __str__(self):
        return self.nombre

        
class Cliente(models.Model):
    rut = models.IntegerField(primary_key=True, verbose_name='Rut')
    nombre = models.CharField(max_length=40, verbose_name='Nombre')
    gmail = models.CharField(max_length=40, verbose_name='gmail')
    telefono = models.IntegerField(verbose_name='telefono', null=True)
    direccion = models.CharField(max_length=50, verbose_name='direccion', null=True)
    def __str__(self):
        return self.nombre
 