"""
第k个素数
"""
import math
def isPrime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def getKPrime(k):
    if k == 1:
        return 2
    n = 100000
    k -= 1
    for i in range(3, n, 2):
        if isPrime(i):
            k -= 1
        if k == 0:
            return i

n = 10000000
is_prime = [True] * n
def getKPrime2(k):
    if k == 1:
        return 2
    k -= 1
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    for i in range(3, n, 2):
        if is_prime[i]:
            k -= 1
        if k == 0:
            return i
import time
s = time.time()
res1 = getKPrime(20000)
e = time.time()
print(res1, e-s)

s = time.time()
res2 = getKPrime2(20000)
e = time.time()
print(res2, e-s)
