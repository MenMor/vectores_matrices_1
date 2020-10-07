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
    suma_c = sum([i[j] ** 3 for i in matriz])  # Creo una lista compuesta para crear w con valores de cada columna
    raiz_c = suma_c ** (1/3)
    raiz_c = round(raiz_c, 2)
    w = np.append(w, raiz_c)


# Generar vectores de forma eficiente. sum(1) suma por filas y .sum(0) suma por columnas
vector_v = np.around(((matriz**2).sum(1)**(1/2)), 2)
vector_w = np.around(((matriz**3).sum(0)**(1/3)), 2)
print(vector_v)
print(vector_w)


# Convierto matriz de int a float
matriz = matriz.astype(float)

# Agrego columna 'v' a matriz
matriz = np.insert(matriz, matriz.shape[1], v, 1)  # shape es para indicar [0] fila o [1] columna que se insertara

print('\n', matriz)
print(w)

a = int(input(" : "))
b = int(input(" : "))
mult = np.sum(np.arange(1, b))
print(mult)

# matriz = np.insert(matriz, matriz.shape[0], w, 0)
