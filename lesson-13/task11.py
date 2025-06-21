import numpy as np

matrix = np.random.randint(1, 10, (3, 3))

determinant = np.linalg.det(matrix)

print(determinant)
