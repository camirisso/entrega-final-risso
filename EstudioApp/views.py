
from pickletools import read_unicodestring8
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Consulta, Cliente, Abogado
from django.urls import reverse_lazy
from EstudioApp.forms import ConsultaFormulario, BusquedaConsulta, ClienteFormulario, CreacionUsuario 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def inicio(request):
    return render(request, "EstudioApp/index.html")

def about(request):
    return render(request, "EstudioApp/about.html")

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

# CRUD
# ABOGADO
# CreateView
class AbogadoCrear(LoginRequiredMixin,CreateView):
    model = Abogado
    success_url = "/EstudioApp/abogados/list"
    fields = ['nombre', 'apellido', 'mail', 'area']


# Listview
class AbogadosLista(ListView):
    model = Abogado
    template_name= 'EstudioApp/abogado_list.html'
 

# Detailview
class AbogadoDetalle(DetailView):
    model = Abogado
    template_name= 'EstudioApp/abogado_detail.html'


# UpdateView
class AbogadoActualizar(UpdateView):
    model = Abogado
    success_url = "/EstudioApp/abogados/list"
    fields = ['nombre', 'apellido', 'mail', 'area']


# DeleteView
class AbogadoBorrar(DeleteView):
    model = Abogado
    success_url = "/EstudioApp/abogados/list"


# CONSULTAS
# Leer 
def consultas_list(request):
    consultas_list = Consulta.objects.all()
    return render (
        request, "EstudioApp/consultas_list.html",
        {'consultas_list': consultas_list}
    )

# Crear
def consulta_create(request):
    if request.method == "POST":   
        formulario_consulta = ConsultaFormulario(request.POST) 
        
        if formulario_consulta.is_valid():
            data = formulario_consulta.cleaned_data
            new_consulta = Consulta(
                nombre=data['nombre'], 
                consulta=data['consulta']
            ) 
            new_consulta.save()
            return redirect('consultas_list')

    formulario_consulta = ConsultaFormulario()
    return render(
        request,"EstudioApp/contact.html",
        {'formulario_consulta': formulario_consulta}
    )
 
# Actualizar
def consulta_update(request, id):

    consulta = Consulta.objects.get(id=id)

    if request.method == "POST":   
        formulario_consulta = ConsultaFormulario(request.POST) 
    
        if formulario_consulta.is_valid():
            data = formulario_consulta.cleaned_data
            consulta.nombre = data['nombre']
            consulta.consulta = data['consulta']
            consulta.save()
            return redirect('consultas_list')

    formulario_consulta = ConsultaFormulario(
        initial={
            'nombre': consulta.nombre,
            'consulta': consulta.consulta
        })
    return render(
        request,"EstudioApp/consulta_update.html",
        {'formulario_consulta': formulario_consulta, 'consulta': consulta}
    )

# Borrar
def consulta_delete(request, id):
    consulta = Consulta.objects.get(id=id)
    consulta.delete()
    
    return redirect('consultas_list')

# CLIENTES
# Leer
def clientes_list(request):
    clientes_list = Cliente.objects.all()
    return render (
        request, "EstudioApp/clientes_list.html",
        {'clientes_list': clientes_list}
    )

# Crear
@login_required
def cliente_create(request):
    if request.method == "POST":   
        formulario_cliente = ClienteFormulario(request.POST) 
        
        if formulario_cliente.is_valid():
            data = formulario_cliente.cleaned_data
            new_cliente = Cliente(
                nombre=data['nombre'], 
                apellido=data['apellido'], 
                mail=data['mail']
            ) 
            new_cliente.save()
            return redirect('clientes_list')

    formulario_cliente = ClienteFormulario()
    return render(
        request,"EstudioApp/client.html",
        {'formulario_cliente': formulario_cliente}
    )
 
# Actualizar
def cliente_update(request, id):

    cliente = Cliente.objects.get(id=id)

    if request.method == "POST":   
        formulario_cliente = ClienteFormulario(request.POST) 
    
        if formulario_cliente.is_valid():
            data = formulario_cliente.cleaned_data
            cliente.nombre = data['nombre']
            cliente.apellido = data['apellido']
            cliente.mail = data['mail']
            cliente.save()
            return redirect('clientes_list')

    formulario_cliente = ClienteFormulario(
        initial={
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            'mail': cliente.mail
        })
    return render(
        request,"EstudioApp/cliente_update.html",
        {'formulario_cliente': formulario_cliente, 'cliente': cliente}
    )

# Borrar
def cliente_delete(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    
    return redirect('clientes_list')


# SIGNUP
def signup_estudio(request):

    if request.method == 'POST':
        form = CreacionUsuario(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request, "EstudioApp/index.html", {'msj': f'Se creó el usuario {username}'})
        else: 
            return render(request, 'EstudioApp/signup.html', {'form': form, 'msj': ''})

    form = CreacionUsuario    
    return render(request, 'EstudioApp/signup.html', {'form': form, 'msj': ''})

# LOGIN
def login_estudio(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return render(request, "EstudioApp/index.html", {'msj': 'Te logueaste correctamente'})

            else:
                return render(request, "EstudioApp/login.html", {'form' : form, 'msj': 'No se autenticó'})
        
        else:
            return render(request, "EstudioApp/login.html", {'form' : form, 'msj' : 'Usuario y/o contraseña incorrectos'})

    else:
        form = AuthenticationForm()
        return render(request, "EstudioApp/login.html", {'form' : form, 'msj': ''})
