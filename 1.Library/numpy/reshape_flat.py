import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("[Original Array]")
print(arr)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

arr_reshaped_1d = arr.reshape(-1)
print("[Reshaped Array to 1D]")
print(arr_reshaped_1d)
# [1 2 3 4 5 6 7 8 9]

arr_reshaped_3x3x1 = arr.reshape(3, 3, 1)
print("[Reshaped Array to 3x3x1]")
print(arr_reshaped_3x3x1)
# [[[1]
#   [2]
#   [3]]
#
#  [[4]
#   [5]
#   [6]]
#
#  [[7]
#   [8]
#   [9]]]

print("[Flat iterator over original array]")
for element in arr.flat:
    print(element, end=' ')
# 1 2 3 4 5 6 7 8 9