'''
3.	Escriba un programa que permita crear una lista de palabras y que, a continuación,
pida dos palabras y sustituya la primera por la segunda en la lista.
'''
num_palabras = int(input("Ingrese el número de palabras que desea agregar a la lista: "))
if num_palabras > 0:
    lista_palabras = []
    for i in range(num_palabras):
        palabra = input(f"Ingrese la palabra #{i+1}: ")
        lista_palabras.append(palabra)
    print("La lista de palabras creada es:")
    print(lista_palabras)
else:
    print("Por favor, ingrese un número mayor que cero")

palabraBusqueda = input("Ingrese la palabra que desea buscar en la lista: ")
palabraSustituta = input("Ingrese la palabra por la cual desea sustituir la palabra encontrada: ")

if palabraBusqueda in lista_palabras:
    for i in range(len(lista_palabras)):
        if lista_palabras[i] == palabraBusqueda:
            lista_palabras[i] = palabraSustituta
    print(f"Todas las apariciones de '{palabraBusqueda}' han sido sustituidas por '{palabraSustituta}' en la lista.")
    print("La lista actualizada es:")
    print(lista_palabras)
else:
    print(f"La palabra '{palabraBusqueda}' no se encuentra en la lista.")

