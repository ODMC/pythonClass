'''
4.	Escriba un programa que permita crear una lista de palabras y que, a continuación,
pida una palabra y elimine esa palabra de la lista.
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

palabraEliminar = input("Ingrese la palabra que desea eliminar de la lista: ")

if palabraEliminar in lista_palabras:
    while palabraEliminar in lista_palabras:
        lista_palabras.remove(palabraEliminar)
    print(f"Todas las apariciones de '{palabraEliminar}' han sido eliminadas de la lista.")
    print("La lista actualizada es:")
    print(lista_palabras)
else:
    print(f"La palabra '{palabraEliminar}' no se encuentra en la lista.")
