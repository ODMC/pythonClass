'''
5.	Escriba un programa que permita crear dos listas de palabras y que,
a continuación, elimine de la primera lista los nombres de la segunda lista.
'''

# Crear la primera lista de palabras
num_palabras = int(input("Ingrese el número de palabras que desea agregar a la primera lista: "))
if num_palabras > 0:
    lista_palabras1 = []
    for i in range(num_palabras):
        palabra = input(f"Ingrese la palabra #{i+1}: ")
        lista_palabras1.append(palabra)
    print("La primera lista de palabras creada es:")
    print(lista_palabras1)
else:
    print("Por favor, ingrese un número mayor que cero")

# Crear la segunda lista de palabras
num_palabras2 = int(input("Ingrese el número de palabras que desea agregar a la segunda lista: "))
if num_palabras2 > 0:
    lista_palabras2 = []
    for i in range(num_palabras2):
        palabra = input(f"Ingrese la palabra #{i+1}: ")
        lista_palabras2.append(palabra)
    print("La segunda lista de palabras creada es:")
    print(lista_palabras2)
else:
    print("Por favor, ingrese un número mayor que cero")

# Eliminar de la primera lista los nombres que están en la segunda lista
for palabra in lista_palabras2:
    while palabra in lista_palabras1:
        lista_palabras1.remove(palabra)

print("La primera lista de palabras después de eliminar las palabras de la segunda lista es:")
print(lista_palabras1)