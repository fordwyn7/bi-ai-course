import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-10, 10, 1000)
y = x * x - 4 * x + 4

plt.plot(x, y, label='$f(x) = 2x^2 - 3x + 1$')
plt.title('Parabola')
plt.xlabel('X')
plt.ylabel('Y')

plt.legend()
plt.show()