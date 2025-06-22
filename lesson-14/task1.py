import numpy as np

@np.vectorize
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

temps_f = np.array([32, 68, 100, 212, 77])
temps_c = fahrenheit_to_celsius(temps_f)

print(temps_c)
