from django.contrib import admin
from .models import Abogado, Cliente, Post, Avatar

# Register your models here.

admin.site.register(Abogado)
admin.site.register(Cliente)
admin.site.register(Post)
admin.site.register(Avatar)