from django.contrib import admin
from .models import Abogado, Cliente, Consulta

# Register your models here.

admin.site.register(Abogado)
admin.site.register(Cliente)
admin.site.register(Consulta)
