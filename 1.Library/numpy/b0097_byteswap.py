import numpy as np

arr = np.array([1, 256, 65536], dtype=np.int32)
print("Original array (little-endian):")
print(arr)
print(arr.dtype)

swapped_arr = arr.byteswap()
print("Array after byteswap:")
print(swapped_arr)

big_endian_arr = swapped_arr.newbyteorder()
print("Array interpreted as big-endian:")
print(big_endian_arr)
print(big_endian_arr.dtype)
