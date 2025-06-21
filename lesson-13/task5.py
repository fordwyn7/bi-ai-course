import numpy as np
import random

random_matrix = np.random.randint(1, 100, (10, 10))
max_value = np.max(random_matrix)
min_value = np.min(random_matrix)   

print("max value:", max_value)
print("min value:", min_value)