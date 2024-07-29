import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x = np.linspace(0, 2 * np.pi, 10)
y = np.linspace(0, 2 * np.pi, 10)
X, Y = np.meshgrid(x, y)
U = 10 * np.cos(X) * np.sin(Y)
V = 10 * np.sin(X) * np.cos(Y)

# 바브 플롯 생성
plt.figure(figsize=(10, 6))
plt.barbs(X, Y, U, V, length=7, barbcolor='b', flagcolor='r', pivot='middle')
"""
X, Y : 1D or 2D array-like, barb locations
U, V : 1D or 2D array-like, The x and y components of the barb shaft.
"""

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Wind Barbs Plot Example')
plt.grid(True)  # Add grid for better visualization
plt.show()
