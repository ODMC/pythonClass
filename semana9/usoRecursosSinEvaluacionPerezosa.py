def numeros_pares_cuadrados_generador(archivo):
    cuadrados_pares = []
    with open(archivo, 'r') as f:
        for linea in f:
            for numero in linea.split():
                num = int(numero)
                if num % 2 == 0:
                    cuadrados_pares.append(num ** 2)
    return cuadrados_pares

def suma_sin_evaluacion_perezosa(lista):
    return sum(lista)

archivo_datos = "C:/Users/omalp/OneDrive/Escritorio/numeros.txt"
cuadrados_pares = numeros_pares_cuadrados_generador(archivo_datos)
suma = suma_sin_evaluacion_perezosa(cuadrados_pares)
print(suma) #Salida: 166616670000