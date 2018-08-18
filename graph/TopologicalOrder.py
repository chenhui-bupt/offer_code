graph = {0: [1, 5], 1: [], 2: [0, 3], 3: [2, 5], 4: [2, 3], 5: [4]}
marked = [False] * len(graph)
onStack = [False] * len(graph)
cycles = []
edgeTo = [-1] * len(graph)
hasCycle = False

def dfs1(graph, v):
    onStack[v] = True
    marked[v] = True
    for w in graph[v]:
        if not marked[w]:
            # edgeTo[w] = v
            dfs1(graph, w)
        elif onStack[w]:
            hasCycle = True
    onStack[v] = False

for v in graph:
    if not marked[v]:
        dfs1(graph, v)
    if hasCycle:
        print("有环")
        break

marked = [False] * len(graph)
reversePost = []
def dfs2(graph, v):
    marked[v] = True
    for w in graph[v]:
        if not marked[w]:
            dfs2(graph, w)
    reversePost.append(v)

if not hasCycle:
    for v in graph:
        if not marked[v]:
            dfs2(graph, v)
    print("拓扑排序是:",reversePost[::-1])
