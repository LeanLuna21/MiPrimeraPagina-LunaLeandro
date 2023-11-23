from django.http import HttpResponse
from django.template import loader

# acá voy a agregar las fx para modificar el template

def saludo_inicial(request):
    return HttpResponse("¡Bienvenido a MoonStore!")