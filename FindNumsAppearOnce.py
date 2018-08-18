# -*- coding:utf-8 -*-
import math
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array:
            return [None, None]
        temp = 0
        for num in array:
            temp ^= num
        if temp == 0:
            return
        index = int(math.log(temp- (temp&(temp-1)), 2))
        num1 = 0
        num2 = 0
        for num in array:
            if (num >> index) & 0x01:
                num1 ^= num
            else:
                num2 ^= num
        return num1, num2

s = Solution()
array = [1,1,2,2,3,3,4,5]
arr2 = [2,4,3,6,3,2,5,5]
res = s.FindNumsAppearOnce(arr2)
print(res)
