import numpy as np

# 원본 배열 생성
arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)
print("Original Array:")
print(arr)
print()

# ctypes 속성을 사용하여 데이터에 접근
data_ptr = arr.ctypes.data
print("Data Pointer (ctypes):")
print(data_ptr)
print()

# ctypes 배열로 변환하여 데이터 읽기
import ctypes

# ctypes 배열 유형 정의 (int32 배열)
c_int_array = ctypes.c_int32 * len(arr)
c_arr = c_int_array.from_address(data_ptr)

print("Array Elements through ctypes:")
for element in c_arr:
    print(element, end=' ')
print("\n")

# ctypes를 사용하여 배열의 값을 변경
c_arr[0] = 10
c_arr[1] = 20
print("Modified Array through ctypes:")
print(arr)
print()

# 다차원 배열 생성
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.float64)
print("Original 2D Array:")
print(arr_2d)
print()

# ctypes 속성을 사용하여 2D 배열 데이터에 접근
data_ptr_2d = arr_2d.ctypes.data
print("Data Pointer for 2D Array (ctypes):")
print(data_ptr_2d)
print()

# ctypes 배열 유형 정의 (float64 배열)
c_double_array = ctypes.c_double * arr_2d.size
c_arr_2d = c_double_array.from_address(data_ptr_2d)

print("2D Array Elements through ctypes (flattened):")
for element in c_arr_2d:
    print(element, end=' ')
print("\n")

# ctypes를 사용하여 2D 배열의 값을 변경
c_arr_2d[0] = 10.0
c_arr_2d[1] = 20.0
print("Modified 2D Array through ctypes:")
print(arr_2d)
print()
