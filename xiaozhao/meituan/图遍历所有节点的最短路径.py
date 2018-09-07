
# N = int(input())
# graph = {}
# for i in range(1, N + 1):
#     graph[i] = []
# for i in range(N - 1):
#     s, e = list(map(int, input().split()))
#     graph[s].append(e)
#     # graph[e].append(s)

N = 4
graph = {1: [2, 3], 3: [4]}
def dfs(s):
    if s not in graph:
        return 0
    else:
        tmp = 0
        for child in graph[s]:
            tmp = max(tmp, dfs(child))
        return tmp + 1
s = 1
res = dfs(s)
print((N - 1) * 2 - res)
