
def countOfZero(n):
    cnt = 0
    while n % 5 == 0:
        cnt += n // 5
        n = n // 5
    return cnt

n = 25
res = countOfZero(n)
print(res)


