import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

covariance_matrix = np.cov(x, y)

print("Covariance matrix:")
print(covariance_matrix)

z = np.array([5, 7, 9, 11, 13])

covariance_matrix_multi = np.cov([x, y, z])

print("Covariance matrix (multiple variables):")
print(covariance_matrix_multi)
