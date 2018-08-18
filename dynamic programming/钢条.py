# -*- coding: utf-8 -*-
"""
钢条切割，收益最大
"""
p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
# 左边切一刀，并假设剩余部分已是最优解
dp = [0] * (len(p) + 1)
for i in range(1, len(dp)):
    for j in range(1, i+1):
        dp[i] = max(dp[i], p[j-1] + dp[i-j])
print(dp)

# 随机切一刀，并假设左右两部分均是最优解
dp = [0] + p
for i in range(1, len(dp)):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[j] + dp[i-j])
print(dp)

# 递归

dp = [0] * (len(p) + 1)


def cut(n):
    if n <= 0:
        return 0
    tmp = 0
    for i in range(1, n+1):
        tmp = max(tmp, cut(n-i) + p[i-1])
    dp[n] = tmp
    return tmp


cut(len(p))
print(dp)



