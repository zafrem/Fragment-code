import numpy as np

# 1. Create two datasets
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

correlation_matrix = np.corrcoef(x, y)

print("[Correlation matrix]")
print(correlation_matrix)

z = np.array([5, 7, 9, 11, 13])

correlation_matrix_multi = np.corrcoef([x, y, z])

print("Correlation matrix (multiple variables)")
print(correlation_matrix_multi)
