# Program to add two matrices
import numpy as np
 

A = [
    [1,2,3],
    [2,3,4],
    [3,4,5]
            ]

B = [
    [15,6,4],
    [7,3,5],
    [0,1,5]
            ]

result = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
            ]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]

print(result)


# Using numpy

arr1 = np.array([[1,2,3],[2,3,4],[4,5,6]])
arr2 = np.array([[5,3,6],[1,4,2],[9,0,5]])

result1 = np.add(arr1,arr2)
print(result1)