n, k = list(map(int, input().split()))
# print(n, k)

tower = list(map(int, input().split()))
# print(tower)

tmax = max(tower)
tmin = min(tower)
diff = tmax - tmin
cnt = 0
res = []
while tmax - tmin > 1 and cnt < k:
    maxInd = tower.index(tmax)
    minInd = tower.index(tmin)
    res.append([maxInd + 1, minInd + 1])
    tower[maxInd] -= 1
    tower[minInd] += 1
    cnt += 1
    tmax = max(tower)
    tmin = min(tower)
tmax = max(tower)
tmin = min(tower)
diff = tmax - tmin
print(diff, cnt)
for re in res:
    print(re[0], re[1])
# print(res)

