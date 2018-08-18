"""
4
4 2
0 1
1 2
2 3
0 2
"""
N = int(input())
M, _ = list(map(int, input().split()))
from collections import defaultdict
graph = defaultdict(list)
for i in range(M):
    s, e = list(map(int, input().split()))
    graph[s].append(e)
root = 0
res = [0]
def dfs(root, graph, res):
    if root in graph:
        childs = graph[root]
        for node in childs:
            res[0] += 1
            dfs(node, graph, res)
dfs(0, graph, res)
print(res[0])
