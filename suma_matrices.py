import numpy as np

a = np.random.randint(10, size=(6, 6))
b = np.random.randint(10, size=(6, 6))
print(a)
print(b)
print(" ")

result = np.random.randint(10, size=(6, 6))
for i in range(len(a)):
    for j in range(len(b)):
        result[i, j] = a[i, j] + b[i, j]

print(result)
print(" ")
print(a+b)


c = np.random.randint(10, size=(6, 6))
print(c)
for i in range(0, len(c)):
    for j in range(0, len(c)):
        c[i, j] = 1  # Remplazar valores de matriz original por otro valor
print(c)

