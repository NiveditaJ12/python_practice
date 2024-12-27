# Program to multiply two matrices

def mul_matrices(mat1,mat2):
    mat3 = [[0,0],[0,0]]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                mat3[i][j] += mat1[i][k] * mat2[k][j]
    return mat3

mat1= [[1,2],
       [4,5]]
mat2 = [[5,3], 
        [3,2]]
print(mul_matrices(mat1,mat2))