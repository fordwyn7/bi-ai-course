import numpy as np

A = np.random.randint(1, 10, (3, 3))
b = np.random.randint(1, 10, (3, 1))
x = np.linalg.solve(A, b)

print(x)
