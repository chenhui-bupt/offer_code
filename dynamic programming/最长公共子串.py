

def longestCommonSubstring(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    dp = []
    for i in range(len1+1):
        dp.append([0] * (len2 + 1))
    maxLen = 0
    res = ""
    for i in range(1, len1+1):
        for j in range(1, len2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = 0
            if maxLen < dp[i][j]:
                maxLen = dp[i][j]
                res = s1[i-maxLen: i]
    return maxLen, res

s1 = "abcdef"
s2 = "acdeg"
res = longestCommonSubstring(s1, s2)
print(res)
