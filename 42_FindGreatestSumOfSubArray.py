# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
        	return
        curSum = 0
        maxSum = -0x80000000
        for num in array:
        	if curSum <= 0:
        		curSum = num
        	else:
        		curSum += num
        	if curSum > maxSum:
        		maxSum = curSum
        return maxSum

s = Solution()
arr = [6,-3,-2,7,-15,1,2,2]
res = s.FindGreatestSumOfSubArray(arr)
print(res)