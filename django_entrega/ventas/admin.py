from django.contrib import admin
# Register your models here.

from ventas.models import Cliente,Transaccion
admin.site.register(Cliente)
admin.site.register(Transaccion)