import numpy as np

matrix1 = np.random.randint(1, 10, (5, 3))
matrix2 = np.random.randint(1, 10, (3, 2))

result_matrix = matrix1 @ matrix2

print(result_matrix)