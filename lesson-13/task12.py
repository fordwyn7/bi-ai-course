import numpy as np

A = np.random.randint(1, 10, (3, 4))
B = np.random.randint(1, 10, (4, 3))
product = A @ B 

print(product)
