import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 10)
y = np.linspace(-5, 5, 10)

X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2

print("[X grid]")
print(X)
print("[Y grid]")
print(Y)
print("[Z grid (Z = X^2 + Y^2)]")
print(Z)

plt.contourf(X, Y, Z, cmap='viridis')
plt.colorbar(label='Z value')
plt.title("Contour plot of Z = X^2 + Y^2")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()
