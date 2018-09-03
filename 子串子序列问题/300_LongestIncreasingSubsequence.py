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
    class Solution(object):
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
                    if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                maxLen = max(maxLen, dp[i])
            return maxLen


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tails = []
        for i in range(len(nums)):
            left, right = 0, len(tails)
            while left < right:
                mid = (left + right) // 2
                if tails[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            if left == len(tails):
                tails.append(nums[i])
            else:
                tails[left] = nums[i]
        return len(tails)


s = Solution()
nums = [4,10,4,3,8,9]
res = s.lengthOfLIS(nums)
print(res)
