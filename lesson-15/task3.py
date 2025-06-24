import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-10, 10, 400)
x2 = np.linspace(-10, 10, 400)
x3 = np.linspace(-2, 2, 400)
x4 = np.linspace(0, 10, 400) 

y1 = x1**3
y2 = np.sin(x2)
y3 = np.exp(x3)
y4 = np.log(x4 + 1)

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
# Top-left: f(x) = x^3
axs[0, 0].plot(x1, y1, color='blue')
axs[0, 0].set_title(r'$f(x) = x^3$')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('f(x)')

# Top-right: f(x) = sin(x)
axs[0, 1].plot(x2, y2, color='green')
axs[0, 1].set_title(r'$f(x) = \sin(x)$')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('f(x)')

# Bottom-left: f(x) = e^x
axs[1, 0].plot(x3, y3, color='red')
axs[1, 0].set_title(r'$f(x) = e^x$')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('f(x)')

# Bottom-right: f(x) = log(x+1)
axs[1, 1].plot(x4, y4, color='purple')
axs[1, 1].set_title(r'$f(x) = \log(x + 1)$')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('f(x)')

plt.tight_layout()
plt.show()
