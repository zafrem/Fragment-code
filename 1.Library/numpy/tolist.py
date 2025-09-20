import numpy as np

print("[1D Array]")
arr_1d = np.array([10, 20, 30, 40, 50])
print(arr_1d)
# [10 20 30 40 50]

print("[1D Array converted to List]")
list_1d = arr_1d.tolist()
print(list_1d)
# [10, 20, 30, 40, 50]

print("[2D Array]")
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print("[2D Array converted to List]")
list_2d = arr_2d.tolist()
print(list_2d)
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("[3D Array]")
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d)
# [[[1 2]
#   [3 4]]
#
#  [[5 6]
#   [7 8]]]

print("[3D Array converted to List]")
list_3d = arr_3d.tolist()
print(list_3d)
# [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]