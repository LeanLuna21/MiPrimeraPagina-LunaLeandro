from django.shortcuts import render
from django.http import HttpResponse
from stock.models import Producto
from stock.forms import ProductoFormulario

# Create your views here.
def productos(request):
    
    if request.method == 'POST':
        mi_formulario = ProductoFormulario(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            producto = Producto(nombre=informacion["nombre"], 
                                medida=informacion["medida"], 
                                color_sable=informacion['color_sable'], 
                                color_luz=informacion['color_luz'], 
                                stock=informacion["stock"], 
                                descripcion=informacion["descripcion"], 
                                precio=informacion["precio"])
            
            producto.save()
            return render(request,'index.html')
    
    else:
        mi_formulario = ProductoFormulario()
        return render (request,'productos.html',{'mi_formulario':mi_formulario})
    

