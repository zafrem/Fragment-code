import numpy as np

arr = np.array([10, 3, 7, 2, 8, 6, 4])

print("Original Array:")
print(arr)

min_value = np.min(arr)
max_value = np.max(arr)

min_index = np.argmin(arr)
max_index = np.argmax(arr)

print(f"Minimum Value: {min_value}")
print(f"Index of Minimum Value: {min_index}")

print(f"Maximum Value: {max_value}")
print(f"Index of Maximum Value: {max_index}")

arr_2d = np.array([[5, 12, 7], [9, 3, 2], [6, 4, 11]])

print("\nOriginal 2D Array:")
print(arr_2d)

min_value_2d = np.min(arr_2d)
max_value_2d = np.max(arr_2d)

min_index_2d = np.argmin(arr_2d)
max_index_2d = np.argmax(arr_2d)

print(f"Minimum Value in 2D Array: {min_value_2d}")
print(f"Index of Minimum Value in 2D Array (flattened): {min_index_2d}")

print(f"Maximum Value in 2D Array: {max_value_2d}")
print(f"Index of Maximum Value in 2D Array (flattened): {max_index_2d}")
