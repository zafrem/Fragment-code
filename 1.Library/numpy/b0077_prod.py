import numpy as np

arr1 = np.array([1, 2, 3, 4])

print("Product of all elements in arr1")
prod_all = np.prod(arr1)
print(prod_all)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print("Product along axis=0 (columns) in arr2")
prod_axis0 = np.prod(arr2, axis=0)
print(prod_axis0)

print("Product along axis=1 (rows) in arr2")
prod_axis1 = np.prod(arr2, axis=1)
print(prod_axis1)
