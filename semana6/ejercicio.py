# Escribir un programa que lea un numero entero positivo n, introducido por el usuario y despues muestre en pantalla
# la suma de los n primeros numero positivos

num=int(input("Ingrese el numero: "))

if num<=0:
    print("El numero es negativo o  cero")
else:
    print(num*(num+1)/2)