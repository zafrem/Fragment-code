import numpy as np

print("[1D Array]")
arr_1d = np.array([10, 20, 30, 40, 50])
print(arr_1d)
# [10 20 30 40 50]

print("[Element at index 2 in 1D array]")
item_1d = arr_1d.item(2)
print(item_1d)
# 30

print("[2D Array]")
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print("[Element at index (1, 1) in 2D array]")
item_2d = arr_2d.item(4)
print(item_2d)
# 5

print("[3D Array]")
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d)
# [3D Array]
# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]

print("[Element at index (1, 0, 1) in 3D array]")
item_3d = arr_3d.item(5)
print(item_3d)
# 6