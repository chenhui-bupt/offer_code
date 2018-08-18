class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return
        i = len(nums) - 1
        while i > 0:  # 找到需要进位的位置，即右边最先出现的前一个数小于后一个数的索引（此时该位置往右一定是降序）
            if nums[i] > nums[i - 1]:
                break
            i -= 1
        if i > 0:
            for j in range(len(nums) - 1, i - 1, -1):  # swap交换，选出被进位的候选中最小的数，依然是在最右侧
                if nums[j] > nums[i - 1]:
                    nums[i - 1], nums[j] = nums[j], nums[i - 1]
                    break
        begin = i  # reverse逆序，因为交换后，从i位开始往后是降序的所以需要逆序变成升序，这样才最小
        end = len(nums) - 1
        while begin < end:
            nums[begin], nums[end] = nums[end], nums[begin]
            begin += 1
            end -= 1