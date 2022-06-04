from optparse import OptionValueError
from pyexpat import model
from ssl import Options
from django.db import models
from django.urls import reverse
from django.utils import timezone 
from django.db import models
import uuid
from django.db import models
import uuid
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


class Cliente(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=30)
    mail=models.EmailField()

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} Mail de contacto: {self.mail}"

class Abogado(models.Model):
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=30)
    mail=models.EmailField()
    area=models.CharField(max_length=45)

    def __str__(self):
        return f"Abogado: {self.nombre} {self.apellido} Mail de contacto: {self.mail} Área de especialidad: {self.area}"

class Post(models.Model):
    titulo = models.CharField(max_length=255)   
    imagen_portada =models.ImageField(null=True, blank=True, upload_to='images/')
    autor = models.ForeignKey(Abogado, on_delete=models.CASCADE)
    publicado = models.DateTimeField(default=timezone.now)
    subtitulo = models.TextField()
    body = RichTextField(blank=True, null=True)
    #models.TextField()

    def __str__(self):
      return self.titulo + ' | ' + str(self.autor)

    def get_absolute_url(self):
       return reverse('article-detail', args=(str(self.id)))
    
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatars', null = True, blank = True)

    def __str__(self):
        return f"Imagen de: {self.user.username}"
    