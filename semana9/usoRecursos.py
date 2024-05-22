def numeros_pares_cuadrados_generador(archivo):
    with open(archivo, 'r') as f:
        for linea in f:
            for numero in linea.split():
                num = int(numero)
                if num % 2 == 0:
                    yield num ** 2

def suma_evaluacion_perezosa(generator):
    return sum(generator)

archivo_datos = "C:/Users/omalp/OneDrive/Escritorio/numeros.txt"
suma = suma_evaluacion_perezosa(numeros_pares_cuadrados_generador(archivo_datos))
print(suma) #Salida: 166616670000