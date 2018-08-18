class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [1] * len(nums)
        LIS = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
            if LIS < dp[i]:
                LIS = dp[i]
        print(dp)
        return LIS

    def lengthOfLIS2(self, nums):  # O(nlogn)
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:   # 二分查找找到左边界
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:  # x <= tails[m]
                    j = m
            tails[i] = x  # 因为原来的tails[i]肯定 >= x, 所以需要替换
            if i == size:
                size += 1
            print(tails)
        return size

    def lengthOfLIS3(self, nums):  # O(nlogn)
        tails = []
        for x in nums:
            i, j = 0, len(tails)
            while i != j:   # 二分查找找到左边界
                m = (i + j) // 2
                if tails[m] < x:
                    i = m + 1
                else:  # x <= tails[m]
                    j = m
            if i == len(tails):
                tails.append(x)
            else:
                tails[i] = x  # 因为原来的tails[i]肯定 >= x, 所以需要替换
        return len(tails)


nums = [4, 5, 6, 3]
s = Solution()
print("lengthOfLIS")
print(s.lengthOfLIS(nums))
res = s.lengthOfLIS2(nums)
print(res)
print(s.lengthOfLIS3(nums))
