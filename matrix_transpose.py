# Find the transpose of matrix

import numpy as np

A = [
    [1,2],
    [3,4],
    [4,2]
]

AT = [[0,0,0],[0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        AT[j][i] = A[i][j]

for i in AT:
    print(i)

# Using numpy

A1 = np.array([[1,2,3],[9,5,8]])
B1 = np.transpose(A1)
for i in B1:
    print(i)