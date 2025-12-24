import numpy as np

#1차원 배열로 생성
arr = np.arange(1,37)
print(arr)
print(arr.size)

#3차원 배열로 변환
arr_3d = arr.reshape((3, 3, 4))
print(arr_3d)

#1차원 배열로 변환
arr_F = arr_3d.flatten()
print(arr_F)