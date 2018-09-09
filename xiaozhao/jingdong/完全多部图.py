isTwoColorable = True
"""
1 3
1 5
2 3
2 5
3 4
4 5
3 5"""
graph = {1:[3,5], 2:[3,5], 3:[4, 5], 4:[5]}

marked = [False] * len(graph)
color = [0] * len(graph)
marked = dict(zip())
isTwoColorable = True
def dfs(graph, v):
    marked[v] = True
    for w in graph[v]:
        if not marked[w]:
            color[w] = 1 - color[v]
            dfs(graph, w)
        elif color[v] == color[w]:
            isTwoColorable = False

for s in graph.keys():
    if not marked[s]:
        dfs(graph, s)

set1, set2 = [], []



