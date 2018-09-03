"""
https://leetcode.com/problems/permutations-ii/description/
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return
        nums.sort()
        used = [False] * len(nums)
        tmplist = []
        res = []
        self.helper(nums, used, tmplist, res)
        return res

    def helper(self, nums, used, tmplist, res):
        if len(tmplist) == len(nums):
            res.append(tmplist[::])
        else:
            for i in range(len(nums)):
                if not used[i]:
                    if i > 0 and nums[i-1] == nums[i] and not used[i-1]:
                        continue
                    used[i] = True
                    tmplist.append(nums[i])
                    self.helper(nums,used, tmplist, res)
                    tmplist.pop()
                    used[i] = False