from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators import csrf

from .forms import AccesorioForm
from .forms import ClienteForm
from .models import Accesorio
from .models import Cliente


# Create your views here.
TEMPLATE_DIRS = (
    'os.path.join(BASE_DIR, "templates"),'
)

def index(request):
    return render(request, "index.html")

def calculadora(request):
    return render(request, "calculadora.html")

def Contacto(request):
    return render(request, "Contacto.html")

def Feriados(request):
    return render(request, "Feriados.html")

def galeria(request):
    return render(request, "galeria.html")

def registracion(request):
    return render(request, "registracion.html")

def somos(request):
    return render(request, "somos.html")

def mostrar(request):
    accesorios = Accesorio.objects.all()
    datos = {
        'accesorios' : accesorios
    }
    return render(request, 'mostrar.html', datos)


def form_accesorio(request): 

    if request.method=='POST':
        accesorio_form = AccesorioForm(request.POST, files=request.FILES)
        if accesorio_form.is_valid():
            accesorio_form.save()
            return redirect ('index')
    else:
        accesorio_form = AccesorioForm()
    return render(request, 'crearAccesorios.html', {'accesorio_form': accesorio_form})


def form_modaccesorio(request, id):
    accesorio = Accesorio.objects.get(idProducto=id)
    datos = {
        'form': AccesorioForm(instance = accesorio)
    }
    if request.method=='POST':
        formulario = AccesorioForm(data=request.POST, instance = accesorio, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect ('mostrar')
        
    return render(request, 'form_modaccesorio.html', datos)

def form_del_accesorio(request,id):
    accesorio = Accesorio.objects.get(idProducto=id)
    accesorio.delete()
    return redirect('mostrar')




def CrearCliente(request): 
    if request.method=='POST':
        cliente_form = ClienteForm(request.POST, files=request.FILES)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect ('index')
    else:
        cliente_form = ClienteForm()
    return render(request, 'Crearcliente.html', {'cliente_form': cliente_form})


def MostrarCliente(request):
    cliente = Cliente.objects.all()
    datos = {
        'cliente' : cliente
    }
    return render(request, 'Mostrarcliente.html', datos)


def EliminarCliente(request,id):
    cliente = Cliente.objects.get(Rut_Cliente=id)
    cliente.delete()
    return redirect('MostrarCliente')





def form_modcliente(request, id):
    cliente = Cliente.objects.get(Rut_Cliente=id)
    datos = {
        'form': ClienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario = ClienteForm(data=request.POST, instance = cliente, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect ('MostrarCliente')
    
    return render(request, 'form_modcliente.html', datos)





def form_modaccesorio(request, id):
    accesorio = Accesorio.objects.get(idProducto=id)
    datos = {
        'form': AccesorioForm(instance = accesorio)
    }
    if request.method=='POST':
        formulario = AccesorioForm(data=request.POST, instance = accesorio, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect ('mostrar')
        
    return render(request, 'form_modaccesorio.html', datos)


