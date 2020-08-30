import numpy as np

lim = int(input("Ingrese límite: "))
suma = 0
leibniz = np.arange(0, lim)
suma += np.sum(((-1)**leibniz) / (2*leibniz+1))
print(f"pi = {suma*4}")
