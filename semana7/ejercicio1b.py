'''
Una jugueteria tiene mucho exito en dos de sus productos: payasos y muñecas. Suele hacer
venta por correo y la empresa de logistica les cobra por peso en cada paquete asi que deben
calcular el peso de los payasos y muñecas que saldran en cada paquete a demanda. Cada payaso
pesa 112g y cada muñeca 75g. Escribir un programa que lea el numero de payasos y muñecas.
'''
#pesos en gramos
pesoPayaso = 112
pesoMuneca = 75
numPayasos = int(input("Ingrese el numero de payasos: "))
while numPayasos < 0:
    print("El número de payasos debe ser positivo")
    numPayasos = int(input("Ingrese el número de payasos nuevamente: "))

numMunecas = int(input("Ingrese el numero de muñecas: "))
while pesoMuneca < 0:
    print("El número de muñecas debe ser positivo")
    pesoMuneca = int(input("Ingrese el número de muñecas nuevamente: "))

print("¡Bienvenido a la juguetería!")
print("Productos en el paquete:")
print("- Payasos:", numPayasos)
print("- Muñecas:", numMunecas)
print("el peso total del paquete es: ",numPayasos*pesoPayaso+numMunecas*pesoMuneca, "gramos")
print("¡Gracias por su compra!")
print("===============================")