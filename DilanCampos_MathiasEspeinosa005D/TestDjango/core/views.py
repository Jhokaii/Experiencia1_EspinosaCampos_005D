
from django.shortcuts import redirect, render
from django.views.decorators import csrf


from .models import  Planta, Cliente
from .forms import ClienteForm, PlantaForms

def index(request):
    plantas= Planta.objects.all()
    return render (request, 'index.html')

def somos(request):
    return render (request, 'somos.html')

def contacto(request):
    return render (request, 'contacto.html')

def galeria(request):
    return render (request, 'galeria.html')

def registro(request):
    return render (request, 'registro.html')   




# Create your views here.
def mostrar(request):
    plantas = Planta.objects.all()

    datos = {
        'plantas' : plantas
    }
    return render(request, 'mostrar.html', datos)


def form_planta(request):
    if request.method=='POST':
        planta_form = PlantaForms(request.POST)
        if planta_form.is_valid():
            planta_form.save()
            return redirect('index')
    else:
        planta_form = PlantaForms()
    return render(request, 'form_crear_planta.html', {'planta_form': planta_form})

def form_modplanta(request, id):
    planta = Planta.objects.get(nombre=id)
    datos ={
        'form': PlantaForms(instance = planta)
    }
    if request.method=='POST':
        formulario = PlantaForms(request.POST, instance = planta)
        if formulario.is_valid():
            formulario.save()
            return redirect('mostrar')
    return render(request, 'form_modplanta.html', datos)

def form_de_planta(request, id):
    planta = Planta.objects.get(nombre=id)
    planta.delete()
    return redirect('mostrar')


# ---------------------------------------------------

def clientes(request):

    clientes = Cliente.objects.all()

    datos = {
        'clientes': clientes
    }

    return render(request, 'clientes.html', datos)

def form_cliente(request):
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect ('index')
    else:
        cliente_form = ClienteForm()
    return render(request, 'form_cliente.html', {'cliente_form': cliente_form})

def form_modcliente(request, id):
    cliente = Cliente.objects.get(rut=id)
    datos = {
        'form': ClienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            return redirect ('clientes')
        
    return render(request, 'form_modcliente.html', datos)

def form_del_cliente(request,id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect('clientes')



