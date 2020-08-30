import numpy as np
matriz = np.arange(12).reshape((3, 4))
print(matriz)

# diagonal = np.arange(matriz[range(0, 4), range(0, 4)])


# Recorrer matriz invertida
matriz = np.array([[0, 1,  2,  3],
                  [4,  5,  6,  7],
                  [8,  9, 10, 11],
                  [0,  8,  7,  6]])
for i in range(len(matriz)):
    for j in range(len(matriz)-1, -1, -1):
        print(matriz[i][j], end='')

# suma de matriz a + b

a = np.random.randint(10, size=(5, 5))
b = np.random.randint(10, size=(5, 5))
c = np.empty((5, 5))

for i in range(len(a)):
    for j in range(len(b)):
        c[i, j] = a[i, j] + b[i, j]

print(a)
print(b)
print(a+b)
print(c)

# agregar fila
#print(np.insert(matriz_1, matriz_1.shape[0], np.array((20, 20, 20, 20, 20, 20)), 0))
#agregar columna
#print(np.insert(matriz_1, matriz_1.shape[0], np.array((20, 20, 20, 20, 20, 20)), 1))
