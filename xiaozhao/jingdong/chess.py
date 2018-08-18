K = 2
X, Y = 3, 3
import numpy as np
dp = np.zeros([10005, 9, 9])
d = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
dp[0][0][0] = 1
for k in range(K):
    for x in range(9):
        for y in range(9):
            if (k, x, y) == (1, 1, 2):
                print(True)
            for dd in d:
                tx = x + dd[0]
                ty = y + dd[1]
                if 0 <= tx <= 8 and 0 <= ty <= 8:
                    print(k+1, tx, ty)
                    dp[k + 1][tx][ty] = (dp[k + 1][tx][ty] + dp[k][x][y]) % 1000000007
print(dp[K][X][Y])


