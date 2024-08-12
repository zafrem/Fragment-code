import numpy as np
import pickle

arr = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)

with open('array_dump.pkl', 'wb') as file:
    arr.dump(file)

with open('array_dump.pkl', 'rb') as file:
    loaded_arr = np.load(file, allow_pickle=True)

print("[Original Array]")
print(arr)

print("[Loaded Array from dump file]")
print(loaded_arr)

print("[Serialized Array to Bytes]")
arr_bytes = arr.dumps()
print(arr_bytes)

restored_arr = pickle.loads(arr_bytes)
print("[Restored Array from Bytes]")
print(restored_arr)
