import numpy as np

arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)

arr.tofile('array_data.bin')
arr.tofile('array_data.txt', sep=",", format="%d")

arr_from_bin = np.fromfile('array_data.bin', dtype=np.int32)
arr_from_txt = np.fromfile('array_data.txt', dtype=np.int32, sep=',')

print("Read from binary file:", arr_from_bin)
print("Read from text file:", arr_from_txt)
