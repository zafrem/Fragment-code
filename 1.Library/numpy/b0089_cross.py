import numpy as np

vector_a = np.array([1, 2, 3])
vector_b = np.array([4, 5, 6])

cross_product = np.cross(vector_a, vector_b)

print("[Cross product of vector_a and vector_b]")
print(cross_product, end='\n\n')

vector_c = np.array([1, 2])
vector_d = np.array([3, 4])

cross_product_2d = np.cross(vector_c, vector_d)

print("[Cross product of vector_c and vector_d]")
print(cross_product_2d, end='\n\n')

vectors_a = np.array([[1, 0, 0], [0, 1, 0]])
vectors_b = np.array([[0, 1, 0], [1, 0, 0]])

cross_products = np.cross(vectors_a, vectors_b)

print("[Cross products of multiple vector pairs]")
print(cross_products)
