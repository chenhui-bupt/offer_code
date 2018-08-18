# -*- coding:utf-8 -*-
class Solution(object):
    # array 二维列表
    def FindNumberOfN(self, target, array):
        # write code here
        if not array or not target:
            return False
        m = len(array)
        n = len(array[0])
        i = m - 1
        j = 0
        while i >= 0 and j < n:
            if array[i][j] == target:
                return True
            elif array[i][j] < target:
                j += 1
            else:
                i -= 1
        return False

    def FindTheLeastNumLargerThanN(self, target, array):
        if not array or not target:
            return False
        m = len(array)
        n = len(array[0])
        i = m - 1
        j = 0
        maxTemp = array[m - 1][n - 1]  # 记录右下角最大的数
        while 0 <= i < m and 0 <= j < n:
            if array[i][j] <= target:  # 如果当前值小于等于目标值，则列j自增1
                j += 1
            else:
                # print(arr[i][j]) # 否则，将这个大的数与最大的数比较并取较小的保存
                maxTemp = min(maxTemp, arr[i][j])
                i -= 1  # 行i自减1
        if maxTemp > target:
            return maxTemp
        else:
            return None  # 如果没找比n大的数返回None

    def FindMedian(self, array):
        if not array:
            return




s = Solution()
arr = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
target = 7
res = s.FindNumberOfN(target, arr)
print(res)
res = s.FindTheLeastNumLargerThanN(target, arr)
print("the least number of larger than target n is: ", res)
