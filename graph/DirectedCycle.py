graph = {0: [1, 5], 1: [], 2: [0, 3], 3: [2, 5], 4: [2, 3], 5: [4]}
marked = [False] * len(graph)
onStack = [False] * len(graph)

graph = {1:[2, 3], 2:[], 3:[],  4:[5,6], 5:[], 6:[7], 7:[4]}
marked = dict(zip(graph.keys(), [False] * len(graph)))
onStack = dict(zip(graph.keys(), [False] * len(graph)))

cycles = []
edgeTo = [-1] * len(graph)
edgeTo = dict(zip(graph.keys(), [-1] * len(graph)))
hasCycle = False


def dfs(graph, v):
    onStack[v] = True
    marked[v] = True
    for w in graph[v]:
        # if cycle:
        #     return
        if not marked[w]:  # 节点w不在marked里面，肯定就不在递归栈onStack里
            edgeTo[w] = v
            dfs(graph, w)
        elif onStack[w]:  # 节点w还在栈里，即上层的父节点还未执行完退出，而在本层递归又遇到，出现环路
            cycle = []
            x = v
            while x != w:
                cycle.append(x)
                x = edgeTo[x]
            cycle.append(w)
            cycle.append(v)
            cycles.append(cycle[::-1])
    onStack[v] = False  # 执行完退出，栈标志为False

for v in graph:
    if not marked[v]:
        dfs(graph, v)
print(cycles)
