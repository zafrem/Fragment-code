import numpy as np

print("[Original Array]")
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print("Base of Original Array:", arr.base)
# None

print("[Array View] (Slice of Original Array)")
arr_view = arr[1:4]
print(arr_view)
print("Base of Array View:", arr_view.base)
# [1 2 3 4 5]

print("[Array Copy] (Deep Copy of Original Array)")
arr_copy = arr.copy()
print(arr_copy)
print("Base of Array Copy:", arr_copy.base)
# None

print("[Original 2D Array]")
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d)
print("Base of Original 2D Array:", arr_2d.base)
# None

print("[2D Array View] (Slice of Original 2D Array)")
arr_2d_view = arr_2d[:, 1:3]
print(arr_2d_view)
print("Base of 2D Array View:", arr_2d_view.base)
# [[1 2 3]
# [4 5 6]
#  [7 8 9]]

print("[2D Array Copy] (Deep Copy of Original 2D Array)")
arr_2d_copy = arr_2d.copy()
print(arr_2d_copy)
print("Base of 2D Array Copy:", arr_2d_copy.base)
# None