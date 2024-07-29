import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
data = [np.random.normal(0, std, 100) for std in range(1, 5)]

plt.boxplot(data, vert=True, patch_artist=True)
"""
notch=True : Shows a notch to show the confidence interval of the median.
vert=False : Displays the box horizontally.
patch_artist=True : Applies a style to fill the box.
"""
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Box Plot Example')
plt.show()
