t = int(raw_input().strip())
for i in range(t):
    N = int(raw_input().strip())
    if N % 2 != 0:
        print('No')
        continue
    j = 1
    while N % 2 !=1:
        j *= 2
        N /= 2
        if N % 2 == 1:
            break
    print(str(int(N)) + ' ' + str(j))