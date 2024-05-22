A = [[1, 2, 3], [4, 5, 6]]
B = [[-1, 0], [0, 1], [1, 1]]
# Se crea la matriz resultado que tendra el mismo numero de filas que A
# y el mismo numero de columnas que B. (2x2)
resultado = [[0] * len(B[0]) for _ in range(len(A))]
# Bucle que recorre las filas de A
for i in range(len(A)):
    # Bucle que recorre las columnas de B
    for j in range(len(B[0])):
        # Bucle que recorre los elementos de la fila A y la columna B
        # para realizar el producto y la suma correspondiente
        for k in range(len(B)):
            # Se suma los productos de los elementos de la fila i de A
            # y la columna j de B
            resultado[i][j] += A[i][k] * B[k][j]

print("El producto de las matrices A y B es:")
for fila in resultado:
    print(fila)