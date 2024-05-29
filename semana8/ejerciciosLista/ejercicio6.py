'''
6.	Escriba un programa que permita crear una lista de palabras y que,
a continuación, cree una segunda lista igual a la primera, pero al revés
(no se trata de escribir la lista al revés, sino de crear una lista distinta).
'''

# Crear la lista de palabras
num_palabras = int(input("Ingrese el número de palabras que desea agregar a la lista: "))
if num_palabras > 0:
    lista_palabras = []
    for i in range(num_palabras):
        palabra = input(f"Ingrese la palabra #{i+1}: ")
        lista_palabras.append(palabra)
    print("La lista de palabras creada es:")
    print(lista_palabras)

    # Crear la segunda lista igual a la primera, pero al revés
    lista_palabras_reversa = lista_palabras[::-1]
    print("La segunda lista de palabras, pero al revés, es:")
    print(lista_palabras_reversa)
else:
    print("Por favor, ingrese un número mayor que cero")


