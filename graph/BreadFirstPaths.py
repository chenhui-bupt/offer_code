# -*- coding: utf-8 -*-

graph = {0: [2, 1, 5], 1: [0, 2], 2: [0, 1, 3, 4], 3: [5, 4, 2], 4: [3, 2], 5: [3, 0]}
s = 0
queue = [s]  # 对列
marked = [False] * len(graph.keys())
marked[s] = True
edgeTo = dict(zip(graph.keys(), [-1] * len(graph.keys())))
while queue:  # breadth first search (bfs)
    v = queue.pop(0)
    marked[v] = True
    for w in graph[v]:
        if not marked[w]:
            queue.append(w)
            edgeTo[w] = v
def pathTo(v):
    if not marked[v]:
        return None
    x = v
    path = []
    while x != s:
        path.append(x)
        x = edgeTo[x]  # 找父节点
    path.append(s)
    return path

for v in graph.keys():
    path = pathTo(v)
    print(path, len(path)-1)

