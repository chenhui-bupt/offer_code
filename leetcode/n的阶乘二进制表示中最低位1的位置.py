def fun(n):
    cnt = 0
    while n:
        cnt += n//2
        n = n//2
    return cnt

n = 5
res = fun(n)
print(res)

