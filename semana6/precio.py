#Escribir un programa que pregunte el nombre el nombre de un producto,su precio y un numero de unidades
# y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 digitos enteros
# y 2 decimales ,el numero de unidades con 3 digitos y el coste total con 8 digitos enteros y 2 decimales
nombreProducto = input("Ingrese el nombre del producto: ")
precioUnitario = float(input("Ingrese el precio unitario del producto: "))
numeroUnidades = int(input("Ingrese el número de unidades: "))
coste_total = precioUnitario * numeroUnidades
cadena_producto = str(nombreProducto)
cadena_precio_unitario = str("{:09.2f}".format(precioUnitario))
cadena_numero_unidades = str("{:03}".format(numeroUnidades))
cadena_coste_total = str("{:011.2f}".format(coste_total))
print(cadena_producto +" "+ cadena_precio_unitario + " " + cadena_numero_unidades +" "+ cadena_coste_total)