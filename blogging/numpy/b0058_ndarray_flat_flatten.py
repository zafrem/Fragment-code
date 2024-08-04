import numpy as np

print("[Original 2D Array]")
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d)

print("Using flat to iterate over the array:")
for element in arr_2d.flat:
    print(element, end=' ')
print("")

# flatten 메서드를 사용하여 배열을 1차원 배열로 변환
arr_flattened = arr_2d.flatten()
print("Flattened Array using flatten method:")
print(arr_flattened)
print()

# 배열을 복사하지 않고 원본 배열을 1차원 배열로 변환
arr_flattened_no_copy = arr_2d.ravel()
print("Flattened Array using ravel method (no copy):")
print(arr_flattened_no_copy)
print()

# 다차원 배열 생성
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("Original 3D Array:")
print(arr_3d)
print()

# 3차원 배열을 1차원 배열로 변환
arr_3d_flattened = arr_3d.flatten()
print("Flattened 3D Array using flatten method:")
print(arr_3d_flattened)
print()
