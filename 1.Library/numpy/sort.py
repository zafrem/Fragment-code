import numpy as np

arr = np.array([5, 3, 8, 6, 7, 2])
arr_2d = np.array([[3, 7, 1], [8, 5, 2]])

sorted_arr = np.sort(arr)
print("Original Array:")
print(arr)
print("Sorted Array:")
print(sorted_arr)

sorted_arr_2d_axis0 = np.sort(arr_2d, axis=0)  # 열별로 정렬
sorted_arr_2d_axis1 = np.sort(arr_2d, axis=1)  # 행별로 정렬

print("Original 2D Array:")
print(arr_2d)
print("Sorted 2D Array along axis 0 (columns):")
print(sorted_arr_2d_axis0)
print("Sorted 2D Array along axis 1 (rows):")
print(sorted_arr_2d_axis1)

sorted_indices = np.argsort(arr)
print("Array:")
print(arr)
print("Indices of Sorted Array:")
print(sorted_indices)

sorted_arr_using_indices = arr[sorted_indices]
print("Sorted Array using Indices:")
print(sorted_arr_using_indices)

sorted_arr = np.array([1, 3, 4, 6, 8])
values_to_insert = np.array([5, 7])

insert_positions = np.searchsorted(sorted_arr, values_to_insert)
print("Sorted Array:")
print(sorted_arr)
print("Values to Insert:")
print(values_to_insert)
print("Positions to Insert:")
print(insert_positions)

extended_array = np.insert(sorted_arr, insert_positions, values_to_insert)
print("Extended Array with Inserted Values:")
print(extended_array)