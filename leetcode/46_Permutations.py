"""
https://leetcode.com/problems/permutations/description/
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return
        res = []
        tmplist = []
        self.helper(nums, tmplist, res)
        return res

    def helper(self, nums, tmplist, res):
        if len(tmplist) == len(nums):
            res.append(tmplist[::])
        else:
            for i in range(len(nums)):
                if nums[i] in tmplist:
                    continue
                tmplist.append(nums[i])
                self.helper(nums, tmplist, res)
                tmplist.pop()

