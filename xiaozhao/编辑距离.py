s1 = input()
s2 = input()


def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    if word1 is None or word2 is None:
        return
    len1 = len(word1)
    len2 = len(word2)
    dp = []
    for i in range(len1 + 1):
        dp.append([0] * (len2 + 1))
    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                a = dp[i - 1][j]
                b = dp[i][j - 1]
                c = dp[i - 1][j - 1]
                dp[i][j] = min(a, b, c) + 1
    return dp[len1][len2]

res = minDistance(s1, s2)
print(res)
if res <= 1:
    print(1)
else:
    print(0)