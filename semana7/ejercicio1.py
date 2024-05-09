'''
Una jugueteria tiene mucho exito en dos de sus productos: payasos y muñecas. Suele hacer
venta por correo y la empresa de logistica les cobra por peso en cada paquete asi que deben
calcular el peso de los payasos y muñecas que saldran en cada paquete a demanda. Cada payaso
pesa 112g y cada muñeca 75g. Escribir un programa que lea el numero de payasos y muñecas.
'''
#pesos en gramos
pesoPayaso = 112
pesoMuneca = 75
numPayasos=int(input("Ingrese el numero de payasos: "))
numMunecas=int(input("Ingrese el numero de muñecas: "))
print("el peso total del paquete es: ",numPayasos*pesoPayaso+numMunecas*pesoMuneca, "gramos")

