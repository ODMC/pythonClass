def numeros_pares_cuadrados(lista):
    return (x ** 2 for x in lista if x % 2 == 0)
def suma_evaluacion_perezosa(generator):
    return sum(generator)

numeros = [1, 2, 3, 4, 5, 6]
suma = suma_evaluacion_perezosa(numeros_pares_cuadrados(numeros))
print(suma)  # Salida: 56
