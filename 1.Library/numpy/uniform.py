import numpy as np

print("Uniformly distributed")
print("Random number between 0 and 1 using np.random.uniform():")
random_number = np.random.uniform()
print(random_number)

print("Random number between -1 and 1 using np.random.uniform(-1, 1):")
random_number_range = np.random.uniform(-1, 1)
print(random_number_range)

print("3x3 Matrix of random numbers between -5 and 5 using np.random.uniform(-5, 5, (3, 3)):")
random_matrix = np.random.uniform(-5, 5, (3, 3))
print(random_matrix)

print("Array of 10 random numbers between 1 and 10 using np.random.uniform(1, 10, 10):")
random_array = np.random.uniform(1, 10, 10)
print(random_array)
