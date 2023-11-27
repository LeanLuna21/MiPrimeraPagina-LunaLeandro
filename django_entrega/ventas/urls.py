from django.urls import path
from ventas.views import *

urlpatterns = [
        path('clientes/',clientes, name="clientes"),
        path('ventas/',ventas, name="ventas")
]