import math
def isPrime(num):
    num1 = math.sqrt(num)
    for i in range(2,num):
        if num%i == 0 :
            return False
    return True

def main():
    a = []
    while True:
        n = int(input())
        a.append(n)
        if n == 0:
            break

    # a = []
    # num = 0
    # while True:
    #     if num ==input()!=0:
    #         a.append(num)
    #     else:break


    length = len(a)

    res = [0] * length
    for i in range(length):
        max = a[i]
        rx = a[i]
        rxx = rx//2 + 1
        for j in range(2, rxx):
            if isPrime(j) and isPrime(max-j):
                res[i] += 1

    for i in range(length):
        print(res[i])
    print("end")

main()
