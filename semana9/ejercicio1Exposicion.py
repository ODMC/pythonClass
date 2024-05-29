def numeros_naturales():
    n=0
    while True:
        yield n
        n+=1

generador = numeros_naturales()
primeros_5_numeros = [next(generador) for i in range(5)]
print(primeros_5_numeros)