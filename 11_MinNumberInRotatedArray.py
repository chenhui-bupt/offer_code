# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotatedArray(self, rotateArray):
        if not rotateArray:
            return
        left = 0
        right = len(rotateArray) - 1
        # if rotateArray[left] < rotateArray[right]:
        #     return rotateArray[left]
        while left < right:
            mid = (left + right) // 2
            if rotateArray[mid] > rotateArray[right]:
                left = mid + 1
            elif rotateArray[mid] == rotateArray[right]:
                right -= 1  # 无法确定最小值在mid的左或是右边，只能一步一步缩小范围
            else:
                right = mid
        return rotateArray[left]

    def recursive(self, rotateArray, left, right):  # 递归实现方法
        if left == right:
            return rotateArray[left]
        mid = (left + right) // 2
        if rotateArray[mid] > rotateArray[right]:
            return self.recursive(rotateArray, mid + 1, right)
        elif rotateArray[mid] < rotateArray[right]:
            return self.recursive(rotateArray, left, mid)
        else:
            return self.recursive(rotateArray, left, right - 1)

s = Solution()
print(s.minNumberInRotatedArray([3, 4, 5, 1, 2]))
print(s.minNumberInRotatedArray([1, 2, 3, 4, 5]))
print(s.minNumberInRotatedArray([1, 1, 1, 0, 1]))
print(s.minNumberInRotatedArray([1, 0, 1, 1, 1]))
print(s.minNumberInRotatedArray([]))
print(s.minNumberInRotatedArray([1]))
