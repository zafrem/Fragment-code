import numpy as np

print("[Original 2D Array]")
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print("Using flat to iterate over the array:")
for element in arr_2d.flat:
    print(element, end=' ')
print()
# 1 2 3 4 5 6 7 8 9

print("[Flattened Array using flatten method]")
arr_flattened = arr_2d.flatten()
print(arr_flattened)
# [1 2 3 4 5 6 7 8 9]

print("[Flattened Array using ravel method (no copy)]")
arr_flattened_no_copy = arr_2d.ravel()
print(arr_flattened_no_copy)
# [1 2 3 4 5 6 7 8 9]

print("[Original 3D Array]")
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d)
# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]

print("[Flattened 3D Array using flatten method]")
arr_3d_flattened = arr_3d.flatten()
print(arr_3d_flattened)
# [1 2 3 4 5 6 7 8]