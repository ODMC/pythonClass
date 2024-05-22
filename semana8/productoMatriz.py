# Definimos las matrices
matriz1 = [[1, 2, 3],
           [4, 5, 6]]

matriz2 = [[-1, 0],
           [0, 1],
           [1, 1]]

resultado = []
for i in range(len(matriz1)):
    fila_resultado = []
    for j in range(len(matriz2[0])):
        suma = 0
        for k in range(len(matriz2)):
            suma += matriz1[i][k] * matriz2[k][j]
        fila_resultado.append(suma)
    resultado.append(fila_resultado)

print("El producto de las matrices es:")
for fila in resultado:
    print(fila)