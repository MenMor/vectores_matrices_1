import numpy as np

def vector_sum(vector):
    sum = 0
    for i in range(len(vector)):
        sum += vector[i]
    return sum

long_vector = int(input("  "))

vector_a = np.random.rand(long_vector)
print(vector_a)
print(vector_sum(vector_a))


def producto_sumas(a, b):
    return np.sum(np.ones(b) + (a-1))

a = int(input("a: "))
b = int(input("b: "))

print(a, "*", b, "=", producto_sumas(a, b))


def get_factorial(numero):
    return np.prod(np.arange(2, numero+1))

valor = float(input("Ingrese valor para calcular factorial: "))
print(f"{valor}! = {get_factorial(valor)}")



def mitad(vec, tam):
    mit = vec[(tam//2)]
    return mit

tam = int(input("long "))
j = np.random.rand(5)
print(j)
print(mitad(j, tam+1))

