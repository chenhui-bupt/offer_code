
def partial_match_table(s):
    match_table = [0] * len(s)
    for i in range(len(s)):
        tmp1 = []
        tmp2 = []
        for j in range(i):
            tmp1.append(s[: j+1])
        for j in range(1, i+1):
            tmp2.append(s[j: i+1])
        maxLen = 0
        for tmp in tmp1:
            if tmp in tmp2 and maxLen < len(tmp):
                maxLen = len(tmp)
        match_table[i] = maxLen
    return match_table

def getNext(s):
    next = [0] * len(s)
    i, j = 1, 0
    while i < len(s):
        if j == 0 or s[i] == s[j]:
            i += 1
            j += 1
            if i < len(s):
                next[i] = j
        else:
            j = next[j]
    return next

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
            j = match_table[j-1]
    return False



s1 = "BBC ABCDAB ABCDABCDABDE"
s2 = "ABCDABD"
print(partial_match_table(s2))
print(getNext(s2))
print(KMP(s1, s2))
