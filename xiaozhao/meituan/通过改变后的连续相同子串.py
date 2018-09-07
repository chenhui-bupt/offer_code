# string s;
# int n, k;
# int deal(char a, char a1) // change a to a1
# {
#     int L = 0, R = 0, change = 0, ans = 1;
#     for (int i = 0; i < n; i++)
#     {
#         if (s[i] == a)
#         {
#             if (change < k)
#             {
#                 change++;
#                 R++;
#             }
#             else
#             {
#                 while (L <= R && s[L] != a) L++;
#                 L++;
#                 R++;
#             }
#         }
#         else R++;
#         ans = max(ans, R - L );
#     }
#     return ans;
# }
n, k = list(map(int, input().split()))
s = input().split()
def helper(s):
    l, r, change, ans = 0, 0, 0, 1
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
        ans = max(ans, r - l)
    return ans

s = "1001010101"
n, k = 10, 2
ans = helper(s)
print(ans)
