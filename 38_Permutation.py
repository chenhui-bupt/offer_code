# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        ss = list(ss)
        res = []
        self.helper(ss, 0, res)
        return sorted(res)

    def helper(self, ss, begin, res):
        if begin == len(ss):
            res.append(''.join(ss))
        else:
            for i in range(begin, len(ss)):
                if i != begin and ss[begin] == ss[i]:  # 去重
                    continue
                ss[begin], ss[i] = ss[i], ss[begin]
                self.helper(ss, begin + 1, res)
                ss[begin], ss[i] = ss[i], ss[begin]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return
        res = []
        tempList = []
        self.helper(nums, tempList, res)
        return res

    def helper(self, nums, tempList, res):
        if len(tempList) == len(nums):
            res.append(tempList[::])
        else:
            for i in range(len(nums)):
                if nums[i] in tempList:
                    continue
                tempList.append(nums[i])
                self.helper(nums, tempList, res)
                tempList.pop()

ss = 'aabc'
S = Solution()
res = S.Permutation(ss)
print(res)
print(len(res))
print(len(set(res)))
