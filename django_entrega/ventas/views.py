from django.shortcuts import render

from ventas.models import Cliente,Transaccion
from ventas.forms import *

# Create your views here.
def clientes(request):
    return render(request, './clientes.html')

def ventas(request):
    return render(request, './ventas.html')