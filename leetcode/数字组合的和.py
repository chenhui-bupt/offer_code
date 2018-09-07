"""
https://leetcode.com/problems/combination-sum/description/
Combination Sum
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates or target is None:
            return
        tmplist = []
        res = []
        self.helper(candidates, target, tmplist, 0, res)
        return res

    def helper(self, candidates, target, tmplist, start, res):
        if target < 0:
            return
        elif target == 0:
            res.append(tmplist[::])
        else:
            for i in range(start, len(candidates)):
                tmplist.append(candidates[i])
                self.helper(candidates, target - candidates[i], tmplist, i, res)  # not i+1, because we can reuse it
                tmplist.pop()
                