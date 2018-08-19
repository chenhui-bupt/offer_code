"""
https://leetcode.com/problems/median-of-two-sorted-arrays/description/
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.



Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if nums1 is None or nums2 is None:
            return
        m = len(nums1)
        n = len(nums2)
        if (m + n) % 2 == 1:
            return self.getKth(nums1, 0, m - 1, nums2, 0, n - 1, (m + n + 1) // 2)
        else:
            return (self.getKth(nums1, 0, m - 1, nums2, 0, n - 1, (m + n + 1) // 2) + self.getKth(nums1, 0, m - 1,
                                                                                                  nums2, 0, n - 1, (
                                                                                                              m + n + 2) // 2)) * 0.5

    def getKth(self, nums1, start1, end1, nums2, start2, end2, k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        if len1 > len2:
            return self.getKth(nums2, start2, end2, nums1, start1, end1, k)
        if len1 == 0:
            return nums2[start2 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])
        new_start1 = min(start1 + k // 2 - 1, end1)
        new_start2 = min(start2 + k // 2 - 1, end2)
        if nums1[new_start1] < nums2[new_start2]:
            return self.getKth(nums1, new_start1 + 1, end1, nums2, start2, end2, k - (new_start1 - start1 + 1))
        else:
            return self.getKth(nums1, start1, end1, nums2, new_start2 + 1, end2, k - (new_start2 - start2 + 1))



s = Solution()
nums1 = [1, 3]
nums2 = [2]
res = s.findMedianSortedArrays(nums1, nums2)
print(res)
