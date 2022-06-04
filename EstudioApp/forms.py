from django import forms
from .models import Post

# CLASE DE FORMULARIO DE CLIENTE

class ClienteFormulario(forms.Form):
    # Campos a completar // Input
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=30)
    mail = forms.EmailField()

# CLASE DE FORMULARIO DE ABOGADO

class AbogadoFormulario(forms.Form):
    # Campos a completar // Input
    nombre = forms.CharField(max_length=20)
    apellido= forms.CharField(max_length=30)
    mail = forms.EmailField()
    area = forms.CharField(max_length=45)

# Formulario de búsqueda

class BusquedaConsulta(forms.Form):
    partial_consulta = forms.CharField(label='Buscador', max_length=30)

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'autor', 'publicado', 'subtitulo', 'body', 'imagen_portada')

        widgets = {
            'titulo': forms.TextInput(),
            'autor': forms.Select(),
            'publicado': forms.TextInput(),
            'subtitulo': forms.TextInput(),
            'body': forms.Textarea(),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'subtitulo', 'body')
        widgets = {
            'titulo': forms.TextInput(),
            'subtitulo': forms.TextInput(),
            'body': forms.Textarea(),
        }

class AvatarFormulario(forms.Form):
  
    imagen = forms.ImageField(required=True)