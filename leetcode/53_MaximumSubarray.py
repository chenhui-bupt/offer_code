"""
https://leetcode.com/problems/maximum-subarray/description/
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        tsum = 0
        maxSum = nums[0]
        for i in range(len(nums)):
            if tsum <= 0:
                tsum = nums[i]
            else:
                tsum += nums[i]
            maxSum = max(maxSum, tsum)
        return maxSum
