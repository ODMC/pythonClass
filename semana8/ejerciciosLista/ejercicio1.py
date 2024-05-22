'''
Escriba un programa que permita crear una lista de palabras.
Para ello, el programa tiene que pedir un número y luego solicitar
ese número de palabras para crear la lista. Por último, el programa
tiene que escribir la lista.
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
    print("Por favor, ingrese un número mayor que cero.")