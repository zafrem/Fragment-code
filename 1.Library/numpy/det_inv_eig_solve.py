#  Matrix operations are new to me, so they don't immediately come to mind, but I use them a lot.

import numpy as np

matrix = np.array([[1, 2], [3, 4]])
determinant = np.linalg.det(matrix)

print("Determinant of the matrix:", determinant)

inverse_matrix = np.linalg.inv(matrix)

print("Inverse of the matrix")
print(inverse_matrix)

matrix = np.array([[1, 2], [2, 1]])

eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues of the matrix")
print(eigenvalues)

print("Eigenvectors of the matrix")
print(eigenvectors)

A = np.array([[3, 1], [1, 2]])
b = np.array([9, 8])

x = np.linalg.solve(A, b)

print("Solution of the linear equations (x)")
print(x)
