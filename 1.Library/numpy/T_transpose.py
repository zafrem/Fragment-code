import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("[Original Array]")
print(arr)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print("[Transposed Array using T]")
arr_transposed_T = arr.T
print(arr_transposed_T)
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]

print("[Transposed Array using transpose function]")
arr_transposed_func = np.transpose(arr)
print(arr_transposed_func)
# [[1 4 7]
#  [2 5 8]
#  [3 6 9]]

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
print("[Original 3D Array]")
print(arr_3d)
# [[[ 1  2  3]
#   [ 4  5  6]]
#
#  [[ 7  8  9]
#   [10 11 12]]
#
#  [[13 14 15]
#   [16 17 18]]]

print("[Transposed 3D Array with axes (1, 0, 2)]")
arr_3d_transposed = arr_3d.transpose(1, 0, 2)
print(arr_3d_transposed)
# [[[ 1  2  3]
#   [ 7  8  9]
#   [13 14 15]]
#
#  [[ 4  5  6]
#   [10 11 12]
#   [16 17 18]]]
