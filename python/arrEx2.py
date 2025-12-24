import numpy as np

arr = np.array([[1, 2, 3],[4, 5, 6]])

arr_T=arr.transpose()
arr_F=arr.flatten()
arr_R=arr.reshape(3, 2)

print(arr)
print(arr_T)
print(arr_F)
print(arr_R)