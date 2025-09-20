import numpy as np

dtype = np.dtype([('field1', np.int32), ('field2', np.float32)])
arr = np.array([(1, 2.5), (3, 4.5), (5, 6.5)], dtype=dtype)

print("Original array:", arr)

field1_data = arr.getfield(np.int32, offset=0)
print("field1 data (int32):", field1_data)

field2_data = arr.getfield(np.float32, offset=4)
print("field2 data (float32):", field2_data)

combined_data = arr.getfield(np.int64)
print("Combined data (int64 interpretation):", combined_data)
