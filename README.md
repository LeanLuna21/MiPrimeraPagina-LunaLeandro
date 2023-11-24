# django_model1
Repositiorio online del entregable #3

Este es un proyecto de tienda online de Sables Laser de Star Wars.

La tienda esta desarrollada con el framework Django, y esta divida en 2 aplicaciones: Stock(de productos) y Ventas(transacciones realizadas).

Consta de 3 modelos: 
    - El modelo Producto(en la app de stock), que define nombre, medida, color, cantidad de stock y precio
    - El modelo Cliente(en la app de ventas), que recibe un nombre, un mail y un dni como atributos.
    - El modelo Transaccion(tambien en la app de ventas), que consta de un numero de transaccion, el cliente, el producto y a cantidad vendida en la transaccion, la fecha de venta y el precio total. Tanto el producto como el cliente estan relacionados a este modelo mediante una clave foranea.
    Por ultimo fue necesario crear una funcion que almacene el calculo del precio total antes de guardar el dato en la BBDD.

