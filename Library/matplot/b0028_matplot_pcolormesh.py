import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = (X**2 + Y - 10)**2 + (X + Y**2 - 10)**2

plt.pcolormesh(X, Y, Z, shading='auto', cmap='coolwarm')

plt.colorbar()
plt.title('pcolormesh')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

plt.show()
