nums = [ 2, 3, 2]
tmax = 0
lastna = (nums[0], 0)  # 拿
lastbuna = (0, -1)  # 不拿，并记录上次拿的位置
for i in range(1, len(nums)):

    if (lastna[0] % 2 == 0 and i - lastna[1] != 2) or (lastna[0] % 2 == 1 and i - lastna[1] != 1):
        tna = (lastna[0] + nums[i], i)
        lastna = tna
    else:
        tbuna = lastbuna
        lastbuna = tbuna
    tmax = max(tmax, lastbuna, lastna)
print(tmax)
