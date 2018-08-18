def rotate(matrix, n):
    for i in range(n//2):
        for j in range(n//2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][n - 1 - i]
            matrix[j][n-1-i] = matrix[n-1-i][n-1-j]
            matrix[n-1-i][n-1-j] = matrix[n-1-j][i]
            matrix[n-1-j][i] = temp
    return matrix
import numpy as np
a = np.arange(16).reshape((4,4))
res = rotate(a, 4)
print(res)
