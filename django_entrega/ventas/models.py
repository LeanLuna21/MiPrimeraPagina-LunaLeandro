from django.db import models
from stock.models import Producto

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    mail = models.EmailField()
    dni = models.IntegerField()

    def __str__(self):
        return f"Cliente: {self.nombre}; Mail: {self.mail}."

class Transaccion(models.Model):
    nro_transaccion = models.IntegerField() 
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,related_name='ventas')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_total = models.FloatField() 
    fecha_de_venta = models.DateField()

    def __str__(self):
        return f"Venta n°: {self.nro_transaccion}; {self.cliente} adquirio {self.producto}."
