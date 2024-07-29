import numpy as np

# 원본 배열 생성
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original Array:")
print(arr)
print()

# 배열을 1차원으로 재구성
arr_reshaped_1d = arr.reshape(-1)
print("Reshaped Array to 1D:")
print(arr_reshaped_1d)
print()

# 배열을 2x3 형태로 재구성
arr_reshaped_2x3 = arr.reshape(2, 3, 1)
print("Reshaped Array to 2x3x1:")
print(arr_reshaped_2x3)
print()

# 배열을 1차원 반복자로 평평하게 순회
print("Flat iterator over original array:")
for element in arr.flat:
    print(element, end=' ')
print()
