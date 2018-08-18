# -*- coding:utf-8 -*-

def AddTwoString(s1, s2, carry=0, padding='left'):
    if len(s1) > len(s2):
        length = len(s1)
        if padding == 'left':
            s2 = ['0'] * (len(s1) - len(s2)) + list(s2)
        else:
            s2 = list(s2) + ['0'] * (len(s1) - len(s2))
    else:
        length = len(s2)
        if padding == 'left':
            s1 = ['0'] * (len(s2) - len(s1)) + list(s1)
        else:
            s1 = list(s1) + ['0'] * (len(s2) - len(s1))
    res = ['0'] * length
    for i in range(length-1, -1, -1):
        curSum = ord(s1[i]) - 48 + ord(s2[i]) - 48 + carry
        if curSum >= 10:
            carry = 1
            curSum -= 10
        else:
            carry = 0
        res[i] = str(curSum)
    i = 0
    while res[i] == '0':
        i += 1
    return ''.join(res[i:]), carry


def Add(s1, s2):
    ind1 = s1.index('.')
    ind2 = s2.index('.')
    res2, carry2 = AddTwoString(s1[ind1 + 1:], s2[ind2 + 1:], padding='right')
    res1, carry1 = AddTwoString(s1[:ind1], s2[:ind2], carry=carry2)
    if carry1:
        return str(carry1) + ''.join(res1) + '.' + ''.join(res2)
    else:
        return ''.join(res1) + '.' + ''.join(res2)


def isDigit(s):
    if not s:
        return False
    ndots = 0
    dot = 0
    for i in range(len(s)):
        if not ('0' <= s[i] <= '9' or s[i] in '+-.'):
            return False
        if s[i] in '+-' and i != 0:
            return False
        if s[i] == '.':
            ndots += 1
            dot = i
    if ndots > 1:
        return False
    return True, dot

res = Add('123.456', '1.5789')
print(res)
