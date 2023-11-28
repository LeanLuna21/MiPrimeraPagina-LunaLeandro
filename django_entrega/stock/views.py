from django.shortcuts import render
from django.http import HttpResponse
from stock.models import Producto
from stock.forms import ProductoFormulario

# Create your views here.
def productos(request):
    
    if request.method == 'POST':   #hacemos esto para saber si tengo que guardar los datos del formulario en el html
        mi_formulario = ProductoFormulario(request.POST)

        if mi_formulario.is_valid():  #el proximo paso es validar si la info traida del html es valida o 
                                                    # no contiene datos invalidos y entra en el modelo que vamos a crear
            informacion = mi_formulario.cleaned_data   # toma del request la info que nos interesa                    
            producto = Producto(nombre=informacion["nombre"],   # asigno a cada atributo del objeto, el valor almacenado 
                                medida=informacion["medida"],                # en la clave del diccionario "informacion"
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
    

