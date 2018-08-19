class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None or target is None:
            return
        dct = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in dct:
                dct[nums[i]] = i
            else:
                return dct[diff], i
        return None
