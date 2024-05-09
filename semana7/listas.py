
cantidadPalabras = int(input("Ingresa la cantidad de palabras que deseas ingresar: "))
palabras = []
for i in range(cantidadPalabras):
    palabra = input(f"Ingrese la palabra {i + 1}: ")
    palabras.append(palabra)
print("Las palabras ingresadas son:")
print(palabras)