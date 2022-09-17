import numpy as np

matrix=np.arange(1,13,1).reshape(3,4)
print(matrix)

answer1=matrix[0,1]
answer2=matrix[2:,:2]
answer3=matrix[matrix<5]
answer4=matrix[[1]]

print(answer1)
print(answer2)
print(answer3)
print(answer4)