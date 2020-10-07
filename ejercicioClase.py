import numpy as np

# wc = np.array(w).reshape(4, 1)  # Convierto vector en matriz 1*1

matriz = np.array([[1, 2, 3, 4],
                    [3, 4, 5, 6],
                    [5, 6, 7, 8],
                    [7, 8, 9, 10]])

v = np.zeros((1, len(matriz)))
for i in range(len(matriz)):
    v[0, i] = np.round(np.sum(matriz[i, :] ** 2) ** (1 / 2), 2)
print(v)

w = np.zeros((1, len(matriz)))
for i in range(len(matriz)):
    w[0, i] = np.round(np.sum(matriz[:, i] ** 2) ** (1 / 3), 2)
print(w)

vector_v = np.around(((matriz**2).sum(1)**(1/2)), 2)
vector_w = np.around(((matriz**2).sum(0)**(1/3)), 2)
print(vector_v)
print(vector_w)

# cambio vector a matriz columna (transpuesta)
vt = np.zeros((len(matriz), 1))
for j in range(len(vt)):
    vt[j, 0] = v[0, j]
print(vt)




