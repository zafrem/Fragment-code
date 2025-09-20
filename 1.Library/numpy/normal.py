import numpy as np
import matplotlib.pyplot as plt

print("Random number from standard normal distribution (mean=0, std=1):")
random_number = np.random.normal()
print(random_number)

print("Random number from normal distribution with mean=5, std=2:")
random_number_custom = np.random.normal(loc=5, scale=2)
print(random_number_custom)

print("2x3 Matrix of random numbers from standard normal distribution:")
random_matrix = np.random.normal(loc=0, scale=1, size=(2, 3))
print(random_matrix)

random_numbers = np.random.normal(loc=0, scale=1, size=10000)
plt.hist(random_numbers, bins=50, density=True, alpha=0.6, color='g')
plt.title("Histogram of 10000 random numbers from standard normal distribution")
plt.xlabel("Value")
plt.ylabel("Density")
plt.show()
