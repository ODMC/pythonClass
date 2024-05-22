'''
2.	Escriba un programa que permita crear una lista de palabras y que, a continuación, pida
una palabra y diga cuántas veces aparece esa palabra en la lista.
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

contador = 0
for palabra in lista_palabras:
    if palabra == palabraBusqueda:
        contador += 1

print(f"La palabra '{palabraBusqueda}' aparece {contador} veces en la lista")
