"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None:
            return
        used_dct = {}  # 记录字符上次出现的位置
        maxLen = 0
        start = 0  # 未重复字符的最早位置
        for i in range(len(s)):
            if s[i] in used_dct and start <= used_dct[s[i]]:  # 即start之后有重复字符
                start = used_dct[s[i]] + 1  # 更新start
            else:
                maxLen = max(maxLen, i - start + 1)  # 否则计算最长未重复长度
            used_dct[s[i]] = i  # 记录或更新每个字符的位置
        return maxLen