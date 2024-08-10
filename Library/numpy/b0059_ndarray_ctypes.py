import numpy as np

print("[Original Array]")
arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)
print(arr)

print("[Data Pointer (ctypes)]")
data_ptr = arr.ctypes.data
print(data_ptr)

import ctypes

c_int_array = ctypes.c_int32 * len(arr)
c_arr = c_int_array.from_address(data_ptr)

print("[Array Elements through ctypes]")
for element in c_arr:
    print(element, end=' ')
print("\n")

c_arr[0] = 10
c_arr[1] = 20
print("[Modified Array through ctypes]")
print(arr)

print("[Original 2D Array]")
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.float64)
print(arr_2d)


print("[Data Pointer for 2D Array] (ctypes)")
data_ptr_2d = arr_2d.ctypes.data
print(data_ptr_2d)

c_double_array = ctypes.c_double * arr_2d.size
c_arr_2d = c_double_array.from_address(data_ptr_2d)

print("[2D Array Elements through ctypes (flattened)]")
for element in c_arr_2d:
    print(element, end=' ')
print("\n")

c_arr_2d[0] = 10.0
c_arr_2d[1] = 20.0
print("[Modified 2D Array through ctypes]")
print(arr_2d)
