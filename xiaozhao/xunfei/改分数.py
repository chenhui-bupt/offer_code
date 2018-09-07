# n, avg = 5, 60
# scores = [59, 20, 30, 90, 100]
# # scores = [59, 20, 10, 10, 100]
# diff = n * avg - sum(scores)
# cnt = 0
# scores = sorted(scores)
# i = 0
# while diff > 0:
#     diff = diff - min(diff, 100 - scores[i])
#     i += 1
#     cnt += 1
# 
# print(cnt)
T = int(input())
for i in range(T):
    n, avg = list(map(int, input().split()))
    scores = list(map(int, input().split()))
    diff = n * avg - sum(scores)
    cnt = 0
    i = 0
    scores = sorted(scores)
    while diff > 0:
        diff = diff - min(diff, 100 - scores[i])
        i += 1
        cnt += 1
    print(cnt)
