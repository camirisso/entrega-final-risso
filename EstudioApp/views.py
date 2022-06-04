
from pickletools import read_unicodestring8
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Avatar, Cliente, Abogado, Post, User
from django.urls import reverse_lazy
from EstudioApp.forms import ClienteFormulario, AvatarFormulario
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import Postform, EditForm


# Create your views here.

def inicio(request):
    return render(request, "EstudioApp/index.html")

def about(request):
    return render(request, "EstudioApp/about.html")


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
class AbogadoBorrar(LoginRequiredMixin, DeleteView):
    model = Abogado
    success_url = "/EstudioApp/abogados/list"

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
@login_required
def cliente_delete(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    
    return redirect('clientes_list')

# POST
class PostView(ListView):
    model = Post
    template_name = 'EstudioApp/posts.html'
    ordering = ['-id']    

# POST DETAIL
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'EstudioApp/article.html'  

# POST CREATION
class AddPostView(CreateView):
    model = Post
    form= Postform()
    template_name = 'EstudioApp/add_post.html' 
    fields = '__all__'

# POST UPDATE
class UpdatePostView(UpdateView):
    model = Post
    form = EditForm
    template_name= 'EstudioApp/update_post.html' 
    fields = ['titulo', 'subtitulo', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name= 'EstudioApp/delete_post.html' 
    success_url = reverse_lazy('posts')

# CREAR AVATAR

@login_required
def agregarAvatar(request):
    if request.method == 'POST':
        miFormulario = AvatarFormulario(request.POST, request.FILES) 
        
        if miFormulario.is_valid():
            u = User.objects.get(username=request.user)        
            avatar = Avatar (user=u, imagen=miFormulario.cleaned_data['imagen']) 
            avatar.save()

            return render(request, "EstudioApp/index.html")

    else: 

        miFormulario= AvatarFormulario() 

    return render(request,"EstudioApp/agregar_avatar.html", {"miFormulario":miFormulario})

