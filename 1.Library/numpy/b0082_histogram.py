import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(0, 1, 1000)
hist, bin_edges = np.histogram(data, bins=10)

print("Histogram values (counts per bin):")
print(hist)
print("Bin edges:")
print(bin_edges)

plt.hist(data, bins=10, alpha=0.6, color='b', edgecolor='black')

plt.title("Histogram of 1000 random numbers from standard normal distribution")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()
