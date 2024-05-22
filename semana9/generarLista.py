
numeros = list(range(1, 10001))
ruta_archivo = "C:/Users/omalp/OneDrive/Escritorio/numeros.txt"
# Escribir la lista en el archivo
with open(ruta_archivo, 'w') as archivo:
    for numero in numeros:
        archivo.write(str(numero) + '\n')
print("Se ha generado y guardado la lista de números en", ruta_archivo)
