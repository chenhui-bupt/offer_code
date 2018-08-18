n = int(raw_input().strip())
growth = 0
maxGrowth = dict()
for i in range(n):
    rule = map(int, raw_input().strip().split())
    if rule[0] == 1:
        for i in range(rule[1], rule[2] + 1):
            maxGrowth[i] = max(maxGrowth.get(i, rule[3]), rule[3])
    elif rule[0] == 2:
        growth += rule[2]
growth += sum(maxGrowth.values())
print(growth)