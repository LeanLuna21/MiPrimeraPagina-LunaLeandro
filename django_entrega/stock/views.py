from django.shortcuts import render
from stock.models import Producto
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def agregar_producto(request):
    producto = Producto(nombre='Sable Obi Wan Kenobi', medida='25cm',color='azul',cantidad_en_stock=5,descripcion='Sable replica del Episodio III: La venganza de los Sith')

    producto.save()

    template = loader.get_template("agregar_producto.html")
   
    doc = template.render({"nombre":producto.nombre,"descripcion":producto.descripcion})

    return HttpResponse(doc)