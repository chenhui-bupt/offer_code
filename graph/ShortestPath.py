def relax(graph, e):
    v, w = e[0], e[1]
    if distTo[w] > distTo[v] + graph[v][w]:
        distTo[w] = distTo[v] + graph[v][w]
        edgeTo[w] = e

def relaxVertex(graph, v):
    for w in graph[v]:
        if distTo[w] > distTo[v] + graph[v][w]:
            distTo[w] = distTo[v] + graph[v][w]
            edgeTo[w] = (v, w)


def dfs(graph, v):
    marked[v] = True
    # relaxVertex(graph, v)  # 松弛顶点
    for w in graph[v]:  # 要先把边松弛好，才能进行递归调用（否则递归的函数会使用未松弛的边来做计算）
        relax(graph, (v, w))  # 松弛边
    for w in graph[v]:
        if not marked[w]:
            dfs(graph, w)

graph = {0: {2: 0.26, 4: 0.28}, 1: {3: 0.29}, 2: {7: .34}, 3: {6: .52}, 4: {7: .37, 5: .35},
         5: {1: .32, 7: .28, 4: .35}, 6: {4: .93, 0: .58, 2: .40}, 7: {3: .39, 5: .28}}
marked = [False] * len(graph)
distTo = [0xffffffff] * len(graph)  # 初始化为最大值
edgeTo = [-1] * len(graph)
s = 0
distTo[s] = 0  # 初始化为0


dfs(graph, s)
print(distTo)
print(edgeTo)
for v in graph:
    x = v
    path = []
    while x != s:
        path.append(str(x))
        e = edgeTo[x]
        if e == -1:
            path = []
            print(x)
            break
        else:
            x = edgeTo[x][0]
    if path:
        path.append(str(s))
        print("%d -> %d:" % (s, v), "->".join(path[::-1]))
        print(distTo[v])
    else:
        print("There is no direct path from %d to %d" % (s, v))

