import numpy as np

matrix = np.random.randint(1, 10, (3, 3))
vector = np.random.randint(1, 10, (3, 1))
product = matrix @ vector 

print(product)
