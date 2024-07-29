import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
Z = (X**2 + Y )**2 + (X + Y**2)**2
levels = [10, 20, 30, 40, 50, 100, 150, 200, 250, 300]

contour = plt.contour(X, Y, Z, levels=levels, cmap='coolwarm')

plt.clabel(contour, inline=True, fontsize=8)
plt.colorbar()
plt.title("Contour Plot")

plt.show()