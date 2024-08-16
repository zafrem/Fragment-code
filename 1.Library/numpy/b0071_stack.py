import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

stacked_axis0 = np.stack((a, b), axis=0)
print("Stacked along axis=0:")
print(stacked_axis0)

stacked_axis1 = np.stack((a, b), axis=1)
print("Stacked along axis=1:")
print(stacked_axis1)

print("Horizontal Stack (1D):")
hstack_result = np.hstack((a, b))
print(hstack_result)

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])

print("Horizontal Stack (2D):")
hstack_result_2d = np.hstack((A, B))
print(hstack_result_2d)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Vertical Stack (1D):")
vstack_result = np.vstack((a, b))
print(vstack_result)

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])

print("Vertical Stack (2D):")
vstack_result_2d = np.vstack((A, B))
print(vstack_result_2d)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Depth Stack (1D to 3D):")
dstack_result = np.dstack((a, b))
print(dstack_result)

A = np.array([[1, 2, 3], [4, 5, 6]])
B = np.array([[7, 8, 9], [10, 11, 12]])

print("Depth Stack (2D to 3D):")
dstack_result_2d = np.dstack((A, B))
print(dstack_result_2d)