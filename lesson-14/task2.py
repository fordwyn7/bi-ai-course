import numpy as np


@np.vectorize
def power(base, exponent):
    return base**exponent


bases = np.array([2, 3, 4, 5])
exponents = np.array([1, 2, 3, 4])

results = power(bases, exponents)

print(results)
