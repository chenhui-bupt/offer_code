p1 = [0, 90]
p3 = [0, 90]
p2 = [100, 200]
p4 = [100, 200]

n = 4
params = [[0, 90], [0, 90], [0, 90], [1, 0], [100, 200], [100, 200], [100, 180], [2, 2]]

def isOverLap(p1, p2, p3, p4):
    if p2[1] > p3[1] and p1[1] < p4[1] and p2[0] > p3[0] and p1[0] < p4[0]:
        return True
    else:
        return False

maxCnt = 0
for i in range(n):
    count = 1
    p1 = params[i]
    p2 = params[n + i]
    for j in range(n):
        if i == j:
            continue
        p3 = params[j]
        p4 = params[n + j]
        if isOverLap(p1, p2, p3, p4):
            count += 1
    if maxCnt < count:
        maxCnt = count

print(maxCnt)

