import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 10)
y = np.linspace(-2, 2, 10)
X, Y = np.meshgrid(x, y)
U = -Y
V = X
magnitude = np.sqrt(U**2 + V**2)

plt.quiver(X, Y, U, V, magnitude, angles='xy', scale_units='xy', scale=1, cmap='cool')

plt.colorbar()
plt.title('Quiver Plot with Arrow and Color Adjusted')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()
