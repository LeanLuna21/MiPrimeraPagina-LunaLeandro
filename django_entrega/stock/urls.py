from django.urls import path
from stock.views import agregar_producto

urlpatterns = [
    path('agregar_producto',agregar_producto, name="agregar_producto")
]