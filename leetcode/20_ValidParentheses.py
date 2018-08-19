"""
https://leetcode.com/problems/valid-parentheses/description/
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None:
            return False
        pairs = {'(': ')', '{': '}', '[': ']'}
        i = 0
        while i < len(s):
            l, r = i, i + 1
            while 0 <= l < r < len(s) and s[l] in pairs and pairs[s[l]] == s[r]:
                s = s[:l] + s[l + 1: r] + s[r + 1:]
                r = l
                l -= 1
                i -= 2
            i += 1
        return len(s) == 0


s = Solution()
res = s.isValid("{[]}")
print(res)