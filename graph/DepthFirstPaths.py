# -*- coding: utf-8 -*-
def dfs(graph, v):
    marked[v] = True
    for w in graph[v]:
        if not marked[w]:
            edgeTo[w] = v  # 子节点指向父节点
            dfs(graph, w)


def pathTo(v):
    if not marked[v]:
        return None
    path = []
    x = v
    while(x != s):
        path.append(x)
        x = edgeTo[x]
    path.append(s)
    return path


graph = {0: [1, 2, 5], 1: [0, 2], 2: [0, 1, 3, 4], 3: [2, 4, 5], 4: [2, 3], 5: [0, 3]}
graph = {0: [2, 1, 5], 1: [0, 2], 2: [0, 1, 3, 4], 3: [5, 4, 2], 4: [3, 2], 5: [3, 0]}
"""
# 节点是否被DFS访问过，即是否存在从s到v的节点
"""
marked = [False for v in graph.keys()]
"""
 子节点指向DFS树中该节点的父节点
（key=child，value=parent，而不是key=parent，value=childs，因为树结构中父节点会有多个子节点，不方便
由child在dfs树中只有一个parent，回溯即可
"""
edgeTo = [-1] * len(graph.keys())
s = 0
dfs(graph, s)
for v in graph.keys():
    if marked[v]:
        print(pathTo(v))
print(edgeTo)


