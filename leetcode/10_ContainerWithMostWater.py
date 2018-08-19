"""
https://leetcode.com/problems/container-with-most-water/description/
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 两头往中间挤
        if height is None:
            return 0
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            h = min(height[left], height[right])
            print((right - left) * h)
            area = max(area, (right - left) * min(height[left], height[right]))
            while left < right and height[left] <= h:  # 当宽度变窄时，只需考虑长板有没有可能容积变大，短板肯定会变小，所以直接略过
                left += 1
            while left < right and height[right] <= h:
                right -= 1
        return area

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 两头往中间挤
        if height is None:
            return 0
        left, right = 0, len(height) - 1
        area = 0
        while left < right:
            h = min(height[left], height[right])
            area = max(area, (right - left) * h)
            if height[left] < height[right]:  # 当宽度变窄时，只需考虑长板有没有可能容积变大，短板肯定会变小，所以直接略过
                left += 1
            else:
                right -= 1
        return area

s = Solution()
height = [1,8,6,2,5,4,8,3,7]
res = s.maxArea(height)
print(res)