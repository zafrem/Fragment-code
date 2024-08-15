import numpy as np

arr = np.array([1, 2, 3, 4, 5])

total_sum = np.sum(arr)
print("Total Sum of Array:")
print(total_sum)

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

sum_axis_0 = np.sum(arr_2d, axis=0)  # 열의 합
sum_axis_1 = np.sum(arr_2d, axis=1)  # 행의 합

print("2D Array:")
print(arr_2d)

print("Sum along axis 0 (columns):")
print(sum_axis_0)

print("Sum along axis 1 (rows):")
print(sum_axis_1)

mean_value = np.mean(arr)
print("Mean of Array:")
print(mean_value)

mean_axis_0 = np.mean(arr_2d, axis=0)  # 열의 평균
mean_axis_1 = np.mean(arr_2d, axis=1)  # 행의 평균

print("Mean along axis 0 (columns):")
print(mean_axis_0)

print("Mean along axis 1 (rows):")
print(mean_axis_1)

median_value = np.median(arr)
print("Median of Array:")
print(median_value)

median_axis_0 = np.median(arr_2d, axis=0)  # 열의 중앙값
median_axis_1 = np.median(arr_2d, axis=1)  # 행의 중앙값

print("Median along axis 0 (columns):")
print(median_axis_0)

print("Median along axis 1 (rows):")
print(median_axis_1)