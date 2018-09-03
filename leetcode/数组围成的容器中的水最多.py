"""
Container with Most Water
"""
class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            h = min(height[left], height[right])
            area = max(area, (right - left) * h)
            while left < right and height[left] <= h:
                left += 1
            while left < right and height[right] <= h:
                right -= 1
        return area

s = Solution()
height = [1,8,6,2,5,4,8,3,7]
height = [1, 8, 100, 2, 3, 16]
res = s.maxArea(height)
print(res)

