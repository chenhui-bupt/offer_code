"""
3
6  3
1  3
2  5
"""

N = int(input())
noodles = []
for i in range(N):
    s, e = list(map(int, input().split()))
    if s > e:
        s, e = e, s
    noodles.append([s, e])

noodles.sort(key=lambda x: x[0])
dp = [1] * N
maxLen = 0
for i in range(N):
    for j in range(i, -1, -1):
        if noodles[j][1] <= noodles[i][0]:
            dp[i] = max(dp[i], dp[j] + 1)
        maxLen = max(maxLen, dp[i])
print(maxLen)


"""
7
1 3
2 5
3 8
4 5
5 6
6 7
7 8
"""
