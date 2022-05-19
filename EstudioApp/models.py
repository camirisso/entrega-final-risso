from pyexpat import model
from django.db import models

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

class Consulta(models.Model):
    nombre=models.CharField(max_length=30)
    consulta=models.CharField(max_length=150)

    def __str__(self):
        return f"Nombre: {self.nombre} Consulta: {self.consulta}"