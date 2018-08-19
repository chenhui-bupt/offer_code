"""
https://leetcode.com/problems/next-permutation/description/
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums is None:
            return
        carry = len(nums) - 1
        while carry > 0 and nums[carry - 1] >= nums[carry]:  # index should be carried
            carry -= 1
        if carry == 0:
            nums[::] = nums[::-1]
        else:
            carry -= 1
            replace = len(nums) - 1
            while replace > 0 and nums[replace] <= nums[
                carry]:  # last index that just larger than nums[carry], for swap/carry
                replace -= 1
            nums[carry], nums[replace] = nums[replace], nums[carry]  # swap first
            nums[carry + 1:] = nums[carry + 1:][::-1]  # reverse later


s = Solution()
nums = [3, 2, 1]
s.nextPermutation(nums)
print(nums)