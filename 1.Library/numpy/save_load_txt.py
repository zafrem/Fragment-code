import numpy as np

arr = np.array([[1.5, 2.5, 3.5], [4.5, 5.5, 6.5], [7.5, 8.5, 9.5]])

np.savetxt('example.txt', arr, delimiter=',', fmt='%.2f', header='Column1, Column2, Column3')

# File
# # Column1, Column2, Column3
# 1.50,2.50,3.50
# 4.50,5.50,6.50
# 7.50,8.50,9.50

print("Array has been saved to 'example.txt'.")
loaded_arr = np.loadtxt('example.txt', delimiter=',', skiprows=1)

print("Loaded Array from 'example.txt':")
print(loaded_arr)
