class Cycle(object):
    """
    不存在环路，要求图中任意两点之间仅存在一条简单路径
    所以在dfs树中，如果v的一个子节点w被访问过并且它又不是节点v的父节点u，
    即u到w之间有多条路径(u->v->w及u->v_else->w)，出现环路
    """
    marked = []
    hasCycle = False

    def __init__(self, graph):
        self.marked = [False] * len(graph.keys())
        # marked = dict(zip(graph.keys(), [False] * len(graph.keys()))
        for s in graph.keys():
            if not self.marked[s]:
                self.dfs(graph, s, s)

    def dfs(self, graph, v, u):
        self.marked[v] = True
        for w in graph[v]:
            if not self.marked[w]:
                self.dfs(graph, w, v)
            elif w != u:
                self.hasCycle = True


graph = {0: [6, 2, 1, 5], 1: [0], 2: [0], 3: [5, 4], 4: [5, 6, 3], 5: [3, 4, 0],
         6: [0, 4], 7: [8], 8: [7], 9: [11, 10, 12], 10: [9], 11: [9, 12], 12: [11, 9]}
cycle = Cycle(graph)
print(cycle.hasCycle)
