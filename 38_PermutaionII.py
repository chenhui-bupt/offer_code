class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return
        nums.sort()
        tempList = []
        used = [False] * len(nums)
        res = []
        self.helper(nums, tempList, used, res)
        return res

    def helper(self, nums, tempList, used, res):
        if len(tempList) == len(nums):
            res.append(tempList[::])
        else:
            for i in range(len(nums)):
                if used[i] or (i > 0 and (nums[i] == nums[i - 1]) and not used[
                        i - 1]):  # 重复的数组只能出现在父子节点递归调用栈，不能在兄弟节点递归调用栈中。
                    continue
                used[i] = True
                tempList.append(nums[i])
                self.helper(nums, tempList, used, res)
                used[i] = False
                tempList.pop()