'''
8.	Escriba un programa que permita crear dos listas de palabras y que,
a continuación, escriba las siguientes listas (en las que no debe haber
repeticiones):
•	Lista de palabras que aparecen en las dos listas.
•	Lista de palabras que aparecen en la primera lista, pero no en la segunda.
•	Lista de palabras que aparecen en la segunda lista, pero no en la primera.
•	Lista de palabras que aparecen en ambas listas.
Nota: Para evitar las repeticiones, el programa deberá empezar eliminando
los elementos repetidos en cada lista.
'''

# Función para eliminar elementos repetidos de una lista
def eliminar_repetidos(lista):
    lista_sin_repetidos = []
    for palabra in lista:
        if palabra not in lista_sin_repetidos:
            lista_sin_repetidos.append(palabra)
    return lista_sin_repetidos

# Crear la primera lista de palabras
num_palabras1 = int(input("Ingrese el número de palabras que desea agregar a la primera lista: "))
if num_palabras1 > 0:
    lista_palabras1 = []
    for i in range(num_palabras1):
        palabra = input(f"Ingrese la palabra #{i+1}: ")
        lista_palabras1.append(palabra)
    print("La primera lista de palabras creada es:")
    print(lista_palabras1)
else:
    print("Por favor, ingrese un número mayor que cero")
    exit()

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
    exit()

# Eliminar elementos repetidos de cada lista
lista_palabras1 = eliminar_repetidos(lista_palabras1)
lista_palabras2 = eliminar_repetidos(lista_palabras2)

# Lista de palabras que aparecen en las dos listas (AnB)
lista_interseccion = [palabra for palabra in lista_palabras1 if palabra in lista_palabras2]

# Lista de palabras que aparecen en la primera lista, pero no en la segunda (A-B)
lista_primera_unica = [palabra for palabra in lista_palabras1 if palabra not in lista_palabras2]

# Lista de palabras que aparecen en la segunda lista, pero no en la primera (B-A)
lista_segunda_unica = [palabra for palabra in lista_palabras2 if palabra not in lista_palabras1]

# Lista de palabras que aparecen en ambas listas (AuB)
lista_union = eliminar_repetidos(lista_palabras1 + lista_palabras2)

# Imprimir las listas resultantes
print("Lista de palabras que aparecen en las dos listas (intersección):")
print(lista_interseccion)

print("Lista de palabras que aparecen en la primera lista, pero no en la segunda:")
print(lista_primera_unica)

print("Lista de palabras que aparecen en la segunda lista, pero no en la primera:")
print(lista_segunda_unica)

print("Lista de palabras que aparecen en ambas listas (unión):")
print(lista_union)

