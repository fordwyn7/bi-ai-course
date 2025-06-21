import numpy as np

matrix = np.random.randint(1, 10, (5, 5))
row_sums = np.sum(matrix, axis=1)
col_sums = np.sum(matrix, axis=0)

print(col_sums)
