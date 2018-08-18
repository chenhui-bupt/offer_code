# -*- coding:utf-8 -*-
import sys

t = int(input().strip())
i = 0

while i < t:
    n = int(input().strip())
    s = input().strip().split()[0]
    ans = 0
    j = 0
    while j < n:
        print(j)
        if s[j] == 'X' or s[j] == 'x':
            j += 1
            continue
        if s[j] == '.':
            ans += 1
        j += 2
    print(ans)
    i += 1


