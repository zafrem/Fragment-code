# ndim: Returns the number of dimensions in the array.
# size: Returns the number of all elements in the array.
# itemsize: Returns the byte size of each element in the array.
# nbytes: Returns the total byte size of all elements in the array.
# base: Checks whether the array is a view of another array.
#        If it is a view, returns the base array.
# dtype: Returns the data type of the array.

import numpy as np

arr_1d = np.array([1, 2, 3, 4, 5], dtype=np.int32)
print("[1D Array]")
print(arr_1d)
print("ndim:", arr_1d.ndim)
print("size:", arr_1d.size)
print("itemsize:", arr_1d.itemsize)
print("nbytes:", arr_1d.nbytes)
print("base:", arr_1d.base)
print("dtype:", arr_1d.dtype)

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.float64)
print("[2D Array]")
print(arr_2d)
print("ndim:", arr_2d.ndim)
print("size:", arr_2d.size)
print("itemsize:", arr_2d.itemsize)
print("nbytes:", arr_2d.nbytes)
print("base:", arr_2d.base)
print("dtype:", arr_2d.dtype)

arr_3d = np.array([[[1, 2, 3], [4, 5, 6]],
                   [[7, 8, 9], [10, 11, 12]],
                   [[13, 14, 15], [16, 17, 18]]], dtype=np.int16)
print("[3D Array]")
print(arr_3d)
print("ndim:", arr_3d.ndim)
print("size:", arr_3d.size)
print("itemsize:", arr_3d.itemsize)
print("nbytes:", arr_3d.nbytes)
print("base:", arr_3d.base)
print("dtype:", arr_3d.dtype)

arr_slice = arr_2d[:, :2]
print("[Slice of 2D Array]")
print(arr_slice)
print("ndim:", arr_slice.ndim)
print("size:", arr_slice.size)
print("itemsize:", arr_slice.itemsize)
print("nbytes:", arr_slice.nbytes)
print("base:", arr_slice.base)
print("dtype:", arr_slice.dtype)
