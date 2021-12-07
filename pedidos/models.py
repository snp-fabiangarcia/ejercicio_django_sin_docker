from django.db import models

class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField()
    telefono=models.CharField(max_length=7)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()
    def __str__(self):
        return 'Producto: {0} - Seccion: {1} - Precio: {2}'.format(self.nombre,self.seccion,self.precio)
    
class Pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
