
# n, k = list(map(int, input().split()))
# s = input().split()
def helper(s):
    l, r, change, ans = 0, 0, 0, 1  # left为1的左边界处，right为1的右边界外，即[left, right)
    for i in range(n):
        if s[i] == '0':
            if change < k:
                change += 1
                r += 1
            else:
                while l <= r and s[l] != '0':
                    l += 1
                l += 1
                r += 1
        else:
            r += 1
        print(i, r)
        ans = max(ans, r - l)
    return ans

s = "1001010101"
n, k = 10, 2
ans = helper(s)
print(ans)
