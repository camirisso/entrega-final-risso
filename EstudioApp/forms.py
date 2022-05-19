from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Crear un formulario en django con una clase

# CLASE DE FORMULARIO DE CONSULTA

class ConsultaFormulario(forms.Form):
    # Campos a completar // Input
    nombre = forms.CharField(max_length=30)
    consulta = forms.CharField(max_length=150)


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

# Formulario registro usuarios

class CreacionUsuario(UserCreationForm):
    mail = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput())
    password2 = forms.CharField(label='Repetir contraseña', widget= forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'mail', 'password1', 'password2']
        help_texts = { k: '' for k in fields }