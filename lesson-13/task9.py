import numpy as np

matrix1 = np.random.randint(1, 10, (3, 3))
matrix2 = np.random.randint(1, 10, (3, 3))

dot_product = np.dot(matrix1, matrix2)

print(dot_product)