from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    medida = models.CharField(max_length=10)
    color_sable = models.CharField(max_length=50)
    color_luz = models.CharField(max_length=50)
    cantidad_en_stock = models.IntegerField()
    descripcion = models.TextField()
    precio = models.FloatField

