"""n级台阶每次可跳1，2， 。。。，m级，问有多少种跳法"""

def func(n, m):
    res = [1]
    for i in range(1, m):
        res.append(sum(res) + 1)
    if n < 1:
        return -1
    if n < m:
        return res[n-1]
    for i in range(m, n+1):
        tmp = sum(res) + 1
        res.pop(0)
        res.append(tmp)
    return res[-1]

