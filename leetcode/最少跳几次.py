"""Jump Game II"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        step = 0
        max = 0
        e = 0
        for i in range(len(nums) - 1):
            max = max(max, i + nums[i])
            if i == e:
                step += 1
                e = max
        return step

