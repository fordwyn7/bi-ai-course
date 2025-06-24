import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 2 * np.pi, 1000)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='Sine Wave', color='blue')
plt.plot(x, y2, label='Cosine Wave', color='orange')
plt.title('Sine and Cosine Waves')
plt.xlabel('X')
plt.ylabel('Y')

plt.legend()
plt.show()