"""
Combination Sum 2

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates or target is None:
            return
        res = []
        tmplist = []
        candidates.sort()
        self.helper(candidates, target, tmplist, res, 0)
        return res

    def helper(self, candidates, target, tmplist, res, start):
        if target < 0:
            return
        elif target == 0:
            res.append(tmplist[::])
            print("----")
        else:
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    print('continue',  start, i)
                    continue
                tmplist.append(candidates[i])
                print(start, i, tmplist)
                self.helper(candidates, target - candidates[i], tmplist, res, i + 1)
                tmplist.pop()

s = Solution()
candidates = [2, 5, 2, 1, 2]
target = 5
res = s.combinationSum2(candidates, target)
print(res)
