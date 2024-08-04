import numpy as np

# C_CONTIGUOUS (C) : The data is in a single, C-style contiguous segment. (Row Priority)
# F_CONTIGUOUS (F) : The data is in a single, Fortran-style contiguous segment. (Columns Priority)
# OWNDATA (O) : The array owns the memory it uses or borrows it from another object.
# WRITEABLE (W) : The data area can be written to.
# ALIGNED (A) : The data and all elements are aligned appropriately for the hardware.
# WRITEBACKIFCOPY (X) : This array is a copy of some other array.
# FNC : F_CONTIGUOUS and not C_CONTIGUOUS.
# FORC : F_CONTIGUOUS or C_CONTIGUOUS (one-segment test).
# BEHAVED (B) : ALIGNED and WRITEABLE.
# CARRAY (CA) : BEHAVED and C_CONTIGUOUS.
# FARRAY (FA) : BEHAVED and F_CONTIGUOUS and not C_CONTIGUOUS.

arr_1d = np.array([1, 2, 3, 4, 5])
print("1D Array Flags:")
print(arr_1d.flags)

arr_2d_C = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array (C-contiguous) Flags:")
print(arr_2d_C.flags)

arr_2d_F = np.array([[1, 2, 3], [4, 5, 6]], order='F')
print("2D Array (F-contiguous) Flags:")
print(arr_2d_F.flags)

arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D Array Flags:")
print(arr_3d.flags)

# Memory sharing
arr_slice = arr_1d[:3]
print("Slice of 1D Array Flags:")
print(arr_slice.flags)

# Independent memory
arr_copy = arr_1d.copy()
print("Copy of 1D Array Flags:")
print(arr_copy.flags)

# Disabel write
arr_1d.setflags(write=False)
print("1D Array Flags After Setting Writeable=False:")
print(arr_1d.flags)

# re-write
arr_1d.setflags(write=True)
print("1D Array Flags After Setting Writeable=True:")
print(arr_1d.flags)
