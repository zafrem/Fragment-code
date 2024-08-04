import numpy as np

# 1D dimensional Array
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array")
print(arr_1d)
print("Shape:", arr_1d.shape)
print("Dimensions:", arr_1d.ndim)

# 2D dimensional Array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array")
print(arr_2d)
print("Shape:", arr_2d.shape)
print("Dimensions:", arr_2d.ndim)

# 3D dimensional Array
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
print("3D Array")
print(arr_3d)
print("Shape:", arr_3d.shape)
print("Dimensions:", arr_3d.ndim)

# 4D dimensional Array
arr_4d = np.random.rand(2, 2, 2, 2)  # 2x2x2x2 배열 생성
print("4D Array")
print(arr_4d)
print("Shape:", arr_4d.shape)
print("Dimensions:", arr_4d.ndim)
