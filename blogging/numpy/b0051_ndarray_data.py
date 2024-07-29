import numpy as np

# 1차원 배열 생성
arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr_1d)
print("Data Buffer:", arr_1d.data)
print("Data in Bytes:", arr_1d.tobytes())
print()

# 2차원 배열 생성
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:")
print(arr_2d)
print("Data Buffer:", arr_2d.data)
print("Data in Bytes:", arr_2d.tobytes())
print()

# 3차원 배열 생성
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]], [[13, 14, 15], [16, 17, 18]]])
print("3D Array:")
print(arr_3d)
print("Data Buffer:", arr_3d.data)
print("Data in Bytes:", arr_3d.tobytes())
print()

# 4차원 배열 생성
arr_4d = np.random.rand(2, 2, 2, 2)  # 2x2x2x2 배열 생성
print("4D Array:")
print(arr_4d)
print("Data Buffer:", arr_4d.data)
print("Data in Bytes:", arr_4d.tobytes())
print()
