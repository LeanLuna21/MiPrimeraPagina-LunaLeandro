from django.urls import path
from stock.views import *

urlpatterns = [
    path('productos/',productos, name="productos")
]