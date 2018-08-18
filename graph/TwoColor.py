class TwoColor(object):
    """
    判断是否是二部图，深度优先搜索，标定节点的颜色即可
    """
    marked = []
    color = []
    isTwoColorable = True

    def __init__(self, graph):
        self.marked = [False] * len(graph)
        self.color = [0] * len(graph)
        # self.isTwoColorable = True
        for s in graph.keys():
            if not self.marked[s]:
                self.dfs(graph, s)

    def dfs(self, graph, v):
        self.marked[v] = True
        for w in graph[v]:
            if not self.marked[w]:
                self.color[w] = 1 - self.color[v]
                self.dfs(graph, w)
            elif self.color[v] == self.color[w]:
                self.isTwoColorable = False
graph = {0: [6, 2, 1, 5], 1: [0], 2: [0], 3: [5, 4], 4: [5, 6, 3], 5: [3, 4, 0],
         6: [0, 4], 7: [8], 8: [7], 9: [11, 10, 12], 10: [9], 11: [9, 12], 12: [11, 9]}
twoCycle = TwoColor(graph)
print(twoCycle.isTwoColorable)

graph = {0: [6, 2, 1, 5], 1: [0, 3], 2: [0], 3: [5, 1], 4: [5, 6], 5: [3, 4, 0],
         6: [0, 4, 7], 7: [6, 8], 8: [7, 10], 9: [11, 10], 10: [8, 9, 12], 11: [9, 12], 12: [11, 10]}
twoCycle = TwoColor(graph)
print(twoCycle.isTwoColorable)
