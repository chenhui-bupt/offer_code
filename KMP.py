"""字符串匹配Knuth-Morris-Pratt算法（KMP)"""

def partial_match_table(s2):
    match_table = []
    for i in range(len(s2)):
        tmp1 = []
        tmp2 = []
        for j in range(i + 1):
            tmp1.append(s2[: j + 1])
        for j in range(1, i + 1):
            tmp2.append(s2[j: i + 1])
        maxMatchLen = 0
        for tmp in tmp1:
            if tmp in tmp2 and len(tmp) > maxMatchLen:
                maxMatchLen = len(tmp)
        match_table.append(maxMatchLen)
    return match_table

def KMP(s1, s2):
    match_table = partial_match_table(s2)
    i, j = 0, 0
    while i < len(s1):
        if j == len(s2):
            return True
        if s1[i] == s2[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            i += (j - match_table[j-1])
            j = 0
    return False



s1 = "BBC ABCDAB ABCDABCDABDE"
s2 = "ABCDABD"
res = KMP(s1, s2)
print(res)
