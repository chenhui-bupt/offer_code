graph = {0: [1, 5], 1: [], 2: [0, 3], 3: [2, 5], 4: [2, 3], 5: [4]}
graph = {1:[2, 3], 2:[], 3:[],  4:[5,6], 5:[], 6:[7], 7:[4]}
n = 7


m, n, k = list(map(int, input().split()))
graph = {}
for i in range(k):
    e, s = list(map(int, input().split()))
    if s not in graph:
        graph[s] = []
    graph[s].append(e)
    if e not in graph:
        graph[e] = []
print(graph)
marked = [False] * (len(graph) +1)
onStack = [False] * (len(graph) + 1)
marked = dict(zip(graph.keys(), [False] * len(graph)))
onStack = dict(zip(graph.keys(), [False] * len(graph)))
cycles = []
edgeTo = dict(zip(graph.keys(), [-1] * len(graph)))
hasCycle = False
res = [False]
def dfs1(graph, v, res):
    onStack[v] = True
    marked[v] = True
    for w in graph[v]:
        if not marked[w]:
            # edgeTo[w] = v
            dfs1(graph, w, res)
        elif onStack[w]:
            hasCycle = True
            res[0] = True
    onStack[v] = False

for v in graph:
    if not marked[v]:
        dfs1(graph, v, res)
    if res[0]:
        print("有环")
        break

marked = dict(zip(graph.keys(), [False] * len(graph)))
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
