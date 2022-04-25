from django import forms

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
    consulta = forms.CharField(max_length=30)
    mail = forms.EmailField()

# CLASE DE FORMULARIO DE ABOGADO

class AbogadoFormulario(forms.Form):
    # Campos a completar // Input
    nombre = forms.CharField(max_length=20)
    consulta = forms.CharField(max_length=30)
    mail = forms.EmailField()
    area = forms.CharField(max_length=45)

# Crear formulario de búsqueda

class BusquedaConsulta(forms.Form):
    partial_consulta = forms.CharField(label='Buscador', max_length=30)