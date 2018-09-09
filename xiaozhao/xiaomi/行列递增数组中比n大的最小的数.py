# -*- coding:utf-8 -*-


class Solution:
    def findTheLeastNumberLargerThanN(self, array, target):
        if not array or target:
            return
        m = len(array)
        n = len(array[0])
        i = m - 1
        j = 0
        maxTemp = array[m - 1][n - 1]  # 右下角最大的数
        while i >=0 and j < n:
            if array[i][j] <= target:
                j += 1
            else:
                maxTemp = min(maxTemp, array[i][j])
                i -= 1
        if maxTemp > target:
            return maxTemp
        else:
            return None


s = Solution()
array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
target = 7
res = s.findTheLeastNumberLargerThanN(array, target)
print(res)
