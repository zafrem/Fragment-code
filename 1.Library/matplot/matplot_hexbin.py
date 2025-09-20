import matplotlib.pyplot as plt
import numpy as np

np.random.seed(0)
x = np.random.randn(10000)
y = np.random.randn(10000)

plt.figure(figsize=(10, 6))
hb = plt.hexbin(x, y, gridsize=50, cmap='Blues')
plt.colorbar(hb, label='Count')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Hexbin Plot Example')
plt.grid(True)  # Add grid for better visualization
plt.show()
