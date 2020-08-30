import numpy as np

matriz = np.random.randint(10, size=(6, 6))
print(matriz)

v = []
for i in range(len(matriz)):
    suma = sum(matriz[i] ** 2)
    raiz = suma ** (1/2)
    raiz = round(raiz, 2)
    v = np.append(v, raiz)


w = []
for j in range(len(matriz)):
    suma_c = sum([i[j] ** 3 for i in matriz])
    raiz_c = suma_c ** (1/3)
    raiz_c = round(raiz_c, 2)
    w = np.append(w, raiz_c)


# Convierto matriz de int a float
matriz = matriz.astype(float)

# Agrego columna 'v' a matriz
matriz = np.insert(matriz, matriz.shape[1], v, 1)

print('\n', matriz)
print(w)



# matriz = np.insert(matriz, matriz.shape[0], w, 0)
