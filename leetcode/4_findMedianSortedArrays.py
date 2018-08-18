class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return
        len1 = len(nums1)
        len2 = len(nums2)
        return (self.getKth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, (len1 + len2 + 1) // 2) +
                self.getKth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, (len1 + len2 + 2) // 2)) * 0.5

    def getKth(self, nums1, start1, end1, nums2, start2, end2, k):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1

        if len1 == 0:
            return nums2[start2 + k - 1]
        if len2 == 0:
            return nums1[start1 + k - 1]
        if k == 1:
            return min(nums1[start1], nums2[start2])
        new_start1 = min(start1 + k // 2 - 1, end1)
        new_start2 = min(start2 + k // 2 - 1, end2)
        if (nums1[new_start1] < nums2[new_start2]):
            return self.getKth(nums1, new_start1 + 1, end1, nums2, start2, end2, k - (new_start1 + 1 - start1))
        else:
            return self.getKth(nums1, start1, end1, nums2, new_start2 + 1, end2, k - (new_start2 + 1 - start2))


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return
        len1 = len(nums1)
        len2 = len(nums2)
        if (len1 + len2) % 2 == 1:
            return self.getKth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, (len1 + len2 + 1) // 2, even=False)
        else:
            return self.getKth(nums1, 0, len1 - 1, nums2, 0, len2 - 1, (len1 + len2 + 1) // 2, even=True)


    def getKth(self, nums1, start1, end1, nums2, start2, end2, k, even=True):
        len1 = end1 - start1 + 1
        len2 = end2 - start2 + 1
        if len1 > len2:
            return self.getKth(nums2, start2, end2, nums1, start1, end1, k)
        if len1 == 0:
            if even:
                return (nums2[start2 + k - 1] + nums2[start2 + k]) * 0.5
            else:
                return nums2[start2 + k - 1]
        if k == 1:
            if even:
                if start1 < end1 and start2 < end2:
                    return (min(max(nums1[start1], nums2[start2]), nums1[start1 + 1], nums2[start2+1])) * 0.5
                elif start1 < end1:
                    return (min(max(nums1[start1], nums2[start2]), nums1[start1 + 1])) * 0.5
                elif start2 < end2:
                    return (min(max(nums1[start1], nums2[start2]), nums2[start2+1])) * 0.5
                else:
                    return None
            else:
                return min(nums1[start1], nums2[start2])
        new_start1 = min(start1 + k // 2 - 1, end1)
        new_start2 = min(start2 + k // 2 - 1, end2)
        if (nums1[new_start1] < nums2[new_start2]):
            return self.getKth(nums1, new_start1 + 1, end1, nums2, start2, end2, k - (new_start1 + 1 - start1), even)
        else:
            return self.getKth(nums1, start1, end1, nums2, new_start2 + 1, end2, k - (new_start2 + 1 - start2), even)
