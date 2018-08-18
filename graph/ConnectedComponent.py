# -*- coding:utf-8 -*-
def dfs(graph, v):
    marked[v] = True
    id[v] = component_id
    for w in graph[v]:
        if not marked[w]:
            dfs(graph, w)


graph = {0: [6, 2, 1, 5], 1: [0], 2: [0], 3: [5, 4], 4: [5, 6, 3], 5: [3, 4, 0],
         6: [0, 4], 7: [8], 8: [7], 9: [11, 10, 12], 10: [9], 11: [9, 12], 12: [11, 9]}
marked = [False] * len(graph.keys())
id = [0] * len(graph)
component_id = 0
for s in graph.keys():
    if not marked[s]:
        dfs(graph, s)
        component_id += 1

print(component_id)
print(id)
print(id[5] == id[6], id[5] == id[9])
