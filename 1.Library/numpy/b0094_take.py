# function is used to select the elements at a specified index in an array and return a new array.

import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print("Original array:", arr)

indices = [0, 2, 4]
selected_elements = np.take(arr, indices)
print("Selected elements (1D):", selected_elements)

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original 2D array")
print(arr_2d)

indices_2d = [0, 2]
selected_rows = np.take(arr_2d, indices_2d, axis=0)
print("Selected rows (axis 0):")
print(selected_rows)

selected_columns = np.take(arr_2d, indices_2d, axis=1)
print("Selected columns (axis 1):")
print(selected_columns)
