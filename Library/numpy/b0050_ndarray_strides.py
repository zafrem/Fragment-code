# Indicates the number of bytes required to move to the next element
# in memory at each dimension of the array.

import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:")
print(arr_1d)
print("Shape:", arr_1d.shape)
print("Strides:", arr_1d.strides)

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:")
print(arr_2d)
print("Shape:", arr_2d.shape)
print("Strides:", arr_2d.strides)

print("==== in memory ====")
y = np.reshape(np.arange(2*3*4), (2,3,4))
print(y)
# array([[[ 0,  1,  2,  3],
#        [ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]],
#       [[12, 13, 14, 15],
#        [16, 17, 18, 19],
#        [20, 21, 22, 23]]])
print(y.strides)
# (48, 16, 4) ## (0>12, 0>4, 0>1)
print(y[1,1,1])
# 17
offset = sum(y.strides * np.array((1,1,1)))
print(offset/y.itemsize)
# 17
x = np.reshape(np.arange(5*6*7*8), (5,6,7,8)).transpose(2,3,1,0)
print(x.strides)
# (32, 4, 224, 1344)
i = np.array([3,5,2,2])
offset = sum(i * x.strides)
print(x[3,5,2,2])
# 813
print(offset / x.itemsize)
# 813
