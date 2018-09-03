"""
数组中出现次数超过一半的数字，士兵推倒游戏
"""

class Solution:
    def MoreThanHalfNum(self, nums):
        if not nums:
            return 0
        res = 0
        count = 0
        for i in range(len(nums)):
            if count == 0:
                res = nums[i]
                count = 1
            elif nums[i] == res:
                count += 1
            else:
                count -= 1
        count = 0
        for num in nums:
            if res == num:
                count += 1
        return res > (len(nums)//2)
