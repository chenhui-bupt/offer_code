"""
32. Longest Valid Parentheses

"""


def longestValidParentheses(self, s):
    if not s:
        return 0
    longest = [0] * len(s)
    maxLen = 0
    for i in range(1, len(s)):
        if s[i] == '(':
            continue
        else:
            if s[i-1] == '(':
                longest[i] = (longest[i-2] if i-2 >= 0 else 0) + 2
            elif s[i-1] == ')' and i - longest[i-1] - 1 >= 0 and s[i-longest[i-1] - 1] == '(':
                longest[i] = longest[i-1] + (longest[i - longest[i-1] - 2] if i - longest[i-1] - 2 >= 0 else 0) + 2
            maxLen = max(maxLen, longest[i])
    return maxLen

