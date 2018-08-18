# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        # write code here
        visited = [0] * cols * rows
        return self.helper(threshold, 0, 0, rows, cols, visited, 0), visited

    def helper(self, threshold, i, j, rows, cols, visited, cnt):
        cnt = 0
        if 0 <= i < rows and 0 <= j < cols and (i / 10 + i % 10 + j / 10 + j % 10) <= threshold and not visited[
                            i * cols + j]:
            visited[i * cols + j] = 1
            cnt = 1 + (self.helper(threshold, i - 1, j, rows, cols, visited, cnt) + \
                       self.helper(threshold, i + 1, j, rows, cols, visited, cnt) + \
                       self.helper(threshold, i, j - 1, rows, cols, visited, cnt) + \
                       self.helper(threshold, i, j + 1, rows, cols, visited, cnt))
        return cnt

s = Solution()
res = s.movingCount(5.1, 10, 10)
print(res[0])
import numpy as np
print(np.reshape(res[1], (10, 10)))

