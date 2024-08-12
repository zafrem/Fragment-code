import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
x = np.linspace(0, 10, 10)
y = np.sin(x)
yerr = np.random.uniform(0.1, 0.3, size=y.shape)

plt.errorbar(x, y, yerr=yerr, fmt='o', capsize=5, capthick=2)
"""
yerr: Error value of the y-axis.
fmt='o': Show data points as circles.
capsize=5: Size of the cap on the error bar.
capthick=2: Thickness of the cap of the error bar.
"""
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Error Bar Plot Example')
plt.grid(True)  # Add grid for better visualization
plt.show()
