'''
7.	Escriba un programa que permita crear una lista de palabras y que,
a continuación, elimine los elementos repetidos (dejando únicamente el
primero de los elementos repetidos).
'''
# Crear la lista de palabras
num_palabras = int(input("Ingrese el número de palabras que desea agregar a la lista: "))
if num_palabras > 0:
    lista_palabras = []
    for i in range(num_palabras):
        palabra = input(f"Ingrese la palabra #{i + 1}: ")
        lista_palabras.append(palabra)
    print("La lista de palabras creada es:")
    print(lista_palabras)

    # Eliminar elementos repetidos, dejando solo la primera aparición
    lista_sin_repetidos = []
    for palabra in lista_palabras:
        if palabra not in lista_sin_repetidos:
            lista_sin_repetidos.append(palabra)

    print("La lista de palabras sin elementos repetidos es:")
    print(lista_sin_repetidos)
else:
    print("Por favor, ingrese un número mayor que cero")
