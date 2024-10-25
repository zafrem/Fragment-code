import numpy as np

arr_3d = np.array([[[1], [2], [3]]])
print("Original 3D array:")
print(arr_3d)
print("Shape of the original array:", arr_3d.shape)

squeezed_arr = np.squeeze(arr_3d)
print("\nSqueezed array:")
print(squeezed_arr)
print("Shape of the squeezed array:", squeezed_arr.shape)

squeezed_arr_axis0 = np.squeeze(arr_3d, axis=0)
print("\nSqueezed array with axis=0:")
print(squeezed_arr_axis0)
print("Shape of the squeezed array with axis=0:", squeezed_arr_axis0.shape)

squeezed_arr_axis2 = np.squeeze(arr_3d, axis=2)
print("\nSqueezed array with axis=2:")
print(squeezed_arr_axis2)
print("Shape of the squeezed array with axis=2:", squeezed_arr_axis2.shape)
