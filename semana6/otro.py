# Escribir un programa que pregunte el nombre del usuario en la consola y un numero entero e imprima por pantalla
# en lineas distintas el nombre del usuario tantas veces el numero introducido

nombre=input("Ingrese el nombre:")
num=int(input("Ingrese el numero:"))
for i in range(num):
    print(nombre)