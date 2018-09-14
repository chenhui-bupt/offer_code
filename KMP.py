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


def getNext(s):
    next = [0] * len(s)
    next[0] = -1
    i, j = 0, -1
    while i < len(s):
        if j == -1 or s[i] == s[j]:
            i += 1
            j += 1
            if i < len(s):
                next[i] = j
        else:
            j = next[j]
    return next


def KMP(s1, s2):
    match_table = partial_match_table(s2)
    next = getNext(s2)
    i, j = 0, 0
    while i < len(s1):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        elif j == 0:
            i += 1
        else:
            j = next[j]
        if j == len(s2):
            return True
    return False


s1 = "BBC ABCDAB ABCDABCDABDE"
s2 = "ABCDABD"
print(partial_match_table(s2))
print(getNext(s2))
res = KMP(s1, s2)
print(res)

s1 = "abcmnabcdefg"
s2 = "abcdefg"
print(partial_match_table(s2))
print(getNext(s2))
res = KMP(s1, s2)
print(res)