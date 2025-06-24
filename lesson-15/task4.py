import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)

colors = np.random.rand(100)
markers = ['o', 's', '^', 'D', 'v']

plt.figure(figsize=(8, 6))
for i in range(5):
    idx = np.arange(i, 100, 5) 
    plt.scatter(x[idx], y[idx], c=colors[idx], marker=markers[i], cmap='viridis', label=f'Marker {markers[i]}')

plt.title('Scatter Plot of 100 Random Points')
plt.xlabel('X')
plt.ylabel('Y')

plt.grid(True)
plt.legend()
plt.show()
