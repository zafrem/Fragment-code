import numpy as np

arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Original 2D array:")
print(arr_2d)

swapped_2d = np.swapaxes(arr_2d, 0, 1)
print("2D array with swapped axes (0 <-> 1):")
print(swapped_2d)

arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]])
print("Original 3D array:")
print(arr_3d)

swapped_3d = np.swapaxes(arr_3d, 0, 2)
print("3D array with swapped axes (0 <-> 2):")
print(swapped_3d)
