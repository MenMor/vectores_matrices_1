#Sumar filas y columnas de una matriz y crear una nueva matriz.

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)


matriz = [[0, 1,  2,  3],
          [4,  5,  6,  7],
          [8,  9, 10, 11],
          [0,  8,  7,  6]]

mostrar_matriz(matriz)

filas = len(matriz)
columnas = len(matriz[0])

for i in range(filas):
    suma = sum(matriz[i])
    matriz[i].append(suma)

print()

mostrar_matriz(matriz)

print()

nueva_fila = []

for j in range(columnas):
    suma = sum([fila[j] for fila in matriz])
    nueva_fila.append(suma)

nueva_fila.append(sum(nueva_fila))

matriz.append(nueva_fila)

mostrar_matriz(matriz)