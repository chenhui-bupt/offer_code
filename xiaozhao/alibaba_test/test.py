# -*- coding:utf-8 -*-
a = [[1, 1, 0, 1, 1, 0, 0], [1, 0, 1, 1, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 1],
     [1, 0, 1, 1, 1, 1, 0], [1, 1, 0, 1, 1, 0, 1]]

# rows = int(raw_input().strip())
# cols = int(raw_input().strip())
# a = []
# for i in range(rows):
#     b = map(int, raw_input().strip().split())
#     a.append(b)
rows = len(a)
cols = len(a[0])
maxCount = 0
maxIndex = [0, 0]
for i in range(rows):
    for j in range(cols):
        if a[i][j] == 1:
            count = 1
            ii = i - 1
            while 0 <= ii and a[ii][j] == 1:
                count += 1
                ii -= 1
            ii = i + 1
            while ii < rows and a[ii][j] == 1:
                count += 1
                ii += 1
            jj = j - 1
            while jj >= 0 and a[i][jj] == 1:
                count += 1
                jj -= 1
            jj = j + 1
            while jj < cols and a[i][jj] == 1:
                count += 1
                jj += 1
            if count > maxCount:
                maxCount = count
                maxIndex = [i + 1, j + 1]
        else:
            continue
print(maxCount, maxIndex)
