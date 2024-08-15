import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

dot_product_1d = np.dot(a, b)
print("Dot Product (1D):")
print(dot_product_1d)

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

dot_product_2d = np.dot(A, B)
print("Dot Product (2D - Matrix Multiplication):")
print(dot_product_2d)

inner_product_1d = np.inner(a, b)
print("Inner Product (1D):")
print(inner_product_1d)

inner_product_2d = np.inner(A, B)
print("Inner Product (2D):")
print(inner_product_2d)

outer_product = np.outer(a, b)
print("Outer Product:")
print(outer_product)
