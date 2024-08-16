import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

concat_1d = np.concatenate((arr1, arr2))
print("Concatenated 1D Array:")
print(concat_1d)

arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])

concat_2d_axis0 = np.concatenate((arr3, arr4), axis=0)
print("\nConcatenated 2D Array along axis=0 (rows):")
print(concat_2d_axis0)

concat_2d_axis1 = np.concatenate((arr3, arr4), axis=1)
print("\nConcatenated 2D Array along axis=1 (columns):")
print(concat_2d_axis1)

arr5 = np.array([[[1, 2], [3, 4]]])
arr6 = np.array([[[5, 6], [7, 8]]])

concat_3d_axis0 = np.concatenate((arr5, arr6), axis=0)
print("\nConcatenated 3D Array along axis=0:")
print(concat_3d_axis0)

concat_3d_axis1 = np.concatenate((arr5, arr6), axis=1)
print("\nConcatenated 3D Array along axis=1:")
print(concat_3d_axis1)
