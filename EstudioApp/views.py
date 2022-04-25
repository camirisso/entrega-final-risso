from django.http import HttpResponse
from django.shortcuts import render
from .models import Consulta, Cliente, Abogado

from EstudioApp.forms import ConsultaFormulario, BusquedaConsulta, ClienteFormulario, AbogadoFormulario

# Create your views here.

def inicio(request):
    return render(request, "EstudioApp/index.html")

def about(request):
    return render(request, "EstudioApp/about.html")

def post(request):
    return render(request, "EstudioApp/post.html")

# FORMULARIO DE CONSULTA

def form(request):
    if request.method == "POST": # Viene por POST?    
        formulario = ConsultaFormulario(request.POST) # Se crea formulario
        if formulario.is_valid(): # La información es válida?
            data = formulario.cleaned_data # Aparecerá la información que estaba en cada input 
            nueva_consulta = Consulta(nombre=data['nombre'], consulta=data['consulta']) 
            nueva_consulta.save()
            return render(request, "EstudioApp/contact.html", {'nueva consulta': nueva_consulta})

        print(request.POST)
        # Crear formulario 
    formulario = ConsultaFormulario()
    return render(request,"EstudioApp/contact.html", {'formulario' : formulario})

# FORMULARIO CLIENTE

def form_cliente(request):
    if request.method == "POST":   
        formulario = ClienteFormulario(request.POST) 
        if formulario.is_valid():
            data = formulario.cleaned_data
            nueva_consulta = Cliente(nombre=data['nombre'], apellido=data['apellido'], mail=data['mail']) 
            nueva_consulta.save()
            return render(request, "EstudioApp/client.html", {'nueva consulta': nueva_consulta})

        print(request.POST)
        # Crear formulario 
    formulario = ClienteFormulario()
    return render(request,"EstudioApp/client.html", {'formulario' : formulario})

# FORMULARIO ABOGADO

def form_abogado(request):
    if request.method == "POST":   
        formulario = AbogadoFormulario(request.POST) 
        if formulario.is_valid():
            data = formulario.cleaned_data
            nueva_consulta = Abogado(nombre=data['nombre'], apellido=data['apellido'], mail=data['mail'], area=data['area']) 
            nueva_consulta.save()
            return render(request, "EstudioApp/lawyer.html", {'nueva consulta': nueva_consulta})

        print(request.POST)
        # Crear formulario 
    formulario = AbogadoFormulario()
    return render(request,"EstudioApp/lawyer.html", {'formulario' : formulario})

# BUSQUEDA PARCIAL DE DATOS SOBRE CONSULTA
def search(request):
    consultas_buscadas = []
    dato = request.GET.get('partial_consulta', None)

    if dato is not None:
        consultas_buscadas = Consulta.objects.filter(consulta__icontains=dato)

    buscador = BusquedaConsulta()
    return render(
        request, "EstudioApp/search.html",
        {'buscador': buscador, 'consultas_buscadas': consultas_buscadas, 'dato': dato}
    )

