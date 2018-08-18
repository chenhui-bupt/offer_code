class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        if len(nums) > 1:
            dp[1] = max(nums[:2])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        return dp[-1]


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        return max(self.robHelper(nums, 0, len(nums) - 2), self.robHelper(nums, 1, len(nums) - 1))

    def robHelper(self, nums, left, right):
        if right - left < 2:
            return max(nums[left], nums[right])
        dp = [0] * (right - left + 1)
        dp[0] = nums[left]
        dp[1] = max(nums[left], nums[left + 1])
        for i in range(left + 2, right + 1):
            dp[i - left] = max(dp[i - left - 2] + nums[i], dp[i - left - 1])
        return dp[-1]
