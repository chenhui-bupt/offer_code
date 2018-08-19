"""
https://leetcode.com/problems/longest-palindromic-substring/description/
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        for i in range(len(s)):
            l, r = i, i  # 中心点不重复
            tmp = self.helper(s, l, r)
            if len(tmp) > len(res):
                res = tmp
            l, r = i, i + 1  # 中心两点重复
            tmp = self.helper(s, l, r)
            if len(tmp) > len(res):
                res = tmp
        return res

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:  # 从中间往两边找回文字符串
            l -= 1
            r += 1
        return s[l + 1: r]

