import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 5)]

plt.figure(figsize=(10, 6))
plt.violinplot(data, showmeans=True, showmedians=True)
"""
showmeans : mean
showmedians : median
"""
plt.xlabel('Group')
plt.ylabel('Value')
plt.title('Violin Plot Example')
plt.grid(True)  # Add grid for better visualization
plt.show()
