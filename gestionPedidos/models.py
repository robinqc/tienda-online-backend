from django.db import models

class Clientes(models.Model):
    nombre = models.CharField(max_length = 30)
    direccion = models.CharField(max_length = 50)
    email = models.EmailField()
    tel = models.CharField

class Articulo(models.Model):
    nombre =  models.CharField(max_length = 30)
    seccion = models.CharField(max_length = 20)
    precio = models.IntegerField()

class Pedidos(models.Model):
    numero = models.IntegerField()
    fecha = models.DateField()
    entregado = models.BooleanField()
