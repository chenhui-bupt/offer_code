"""
https://leetcode.com/problems/longest-increasing-subsequence/description/

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
"""
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        maxLen = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    maxLen = max(maxLen, dp[i])

        return maxLen

class Solution(object):
    """
    用ends数组来保存单调序列，这个序列并不是 最优值的单调序列，对于arr[i],如果比 ends 中的每个

    数都大时放到 ends 后面，否则用arr[i]代替ends数组中第一个比arr[i]大的数，保持 ends 递增。这样

    每一个arr[i]在ends的位置就是 dp[i] 的值。
    """
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ends = [0] * len(nums)
        size = 0
        for num in nums:
            left, right = 0, size
            while left < right:
                mid = (left + right) // 2
                if ends[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            ends[left] = num  # 找到ends中最后一个不大于num的位置，需要替换
            # dp[i] = left + 1
        if left == size:
            size += 1
        return size
