import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])
print("Original array:", arr)

condition = np.array([True, False, True, False, True, False])

compressed_arr = np.compress(condition, arr)
print("Compressed array (based on condition):", compressed_arr)

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original 2D array")
print(arr_2d)

condition_2d = np.array([True, False, True])

compressed_arr_2d = np.compress(condition_2d, arr_2d, axis=0)
print("Compressed 2D array (based on condition along axis 0)")
print(compressed_arr_2d)

compressed_arr_2d_axis = np.compress([True, False, True], arr_2d, axis=1)
print("Compressed 2D array (based on condition along axis)")
print(compressed_arr_2d_axis)
