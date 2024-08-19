import numpy as np

arr = np.array([1, 2, 3])
repeated_arr = np.repeat(arr, 3)

print("Original Array")
print(arr)

print("Repeated Array")
print(repeated_arr)

print("Original 2D Array")
arr_2d = np.array([[1, 2], [3, 4]])
print(arr_2d)

repeated_2d_axis0 = np.repeat(arr_2d, 2, axis=0)
repeated_2d_axis1 = np.repeat(arr_2d, 2, axis=1)
print("Repeated 2D Array along axis=0 (rows)")
print(repeated_2d_axis0)
print("Repeated 2D Array along axis=1 (columns)")
print(repeated_2d_axis1)

arr = np.array([1, 2, 3])
print("Tiled 1D Array")
tiled_arr = np.tile(arr, 3)
print(tiled_arr)

print("Original 2D Array")
arr_2d = np.array([[1, 2], [3, 4]])
print(arr_2d)

print("Tiled 2D Array (2x3 times)")
tiled_2d = np.tile(arr_2d, (2, 3))
print(tiled_2d)
