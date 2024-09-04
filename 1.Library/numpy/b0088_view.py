import numpy as np

arr = np.array([1, 2, 3, 4], dtype=np.int8)
view_arr = arr.view(dtype=np.uint8)
print("Original array:", arr, arr.dtype)
print("View of the array as uint8:", view_arr, view_arr.dtype)

arr[0] = 127
print("Modified original array:", arr)
print("View after modifying the original array:", view_arr)

view_arr_2d = arr.view().reshape(2, 2)
print("[View of the array as 2D]")
print(view_arr_2d)

