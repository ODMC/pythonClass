'''
Escribir una funcion que aplique un descuento a un precio y otra que aplique el igv
a un precio. Escribir una tercera funcion que reciba un diccionario con los precios y
porcentajes de una cesta de la compra, y una de las funciones anteriores, y utilice la
funcion pasada para aplicar los descuentos o el IVA a los productos de la cesta y
devolver el precio final de la cesta.
'''
# diccionario de precio con su respectivo porcentaje de descuento
diccionario = {50:20, 30:5, 45:10}

def descuento(precio, porcentajeDescuento):
    return precio - precio * porcentajeDescuento / 100


def igv(precio, porcentajeIgv):
    return precio * 18 / 100


def funcionDiccionario(cesta, funcion):
    total = 0
    for precio,porcentaje in cesta.items():
        total+=funcion(precio,porcentaje)
    return total


print("El precio con descuento es " + str(funcionDiccionario(diccionario, descuento)))
print("El igv es " + str(funcionDiccionario(diccionario, igv)))


print("El total es: " + str(funcionDiccionario(diccionario, igv)+funcionDiccionario(diccionario, descuento) ))


