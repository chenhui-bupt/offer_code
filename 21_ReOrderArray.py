# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):  # 冒泡法
        # write code here
        if array is None:
            return
        if len(array) < 1:
            return array
        n = len(array)
        for i in range(0, n):
            for j in range(0, n-1):
                if self.isEven(array[j]) and not self.isEven(array[j + 1]):
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array
    
    def isEven(self, num):
        return (num & 0x01) == 0

    def reOrderArray2(self, array):
        # write code here
        if not array:
            return []
        i, j = 0, 0
        while j < len(array):
            while i < len(array) and (array[i]%2 != 0):
                i += 1
            j = i + 1
            while j < len(array) and (array[j]%2 == 0):
                j += 1
            if j < len(array):
                temp = array[j]
                for k in range(j, i, -1):
                    array[k] = array[k-1]
                array[i] = temp
        return array


s = Solution()
array = [1,2,3,4,5,6,7]
arr1 = [1,3,5,7]
arr2 = [2,4,6,8]
res = s.reOrderArray(array)
print(res)
print(s.reOrderArray(arr1))
print(s.reOrderArray2(arr2))