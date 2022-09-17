import numpy as np

print("2차원 array")
matrix=np.array(range(1,16))
matrix.shape=3,5
print(matrix)

print(type(matrix))
print(matrix.ndim)
print(matrix.shape)
print(matrix.size)

print(matrix.dtype)
print(matrix.astype('str'))
print(matrix[2,3])
print(matrix[0:2,1:4])