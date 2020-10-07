import numpy as np


def tablero(matriz):
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if i % 2 != 0:
                if j % 2 != 0:
                    matriz[i, j] = 1  # 1 = Blanco y 0 = Negro
            else:
                if j % 2 == 0:
                    matriz[i, j] = 1
    return matriz

matriz = np.zeros((8, 8))
print(tablero(matriz))


def movimiento_alfil(matriz):
    posicion_fila = np.random.randint(7)
    posicion_columna = np.random.randint(7)

print(movimiento_alfil(tablero(matriz)))