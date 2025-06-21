import numpy as np

matrix = np.random.rand(5, 5)

normalized_matrix = (matrix - matrix.min()) / (matrix.max() - matrix.min())

print(normalized_matrix)
