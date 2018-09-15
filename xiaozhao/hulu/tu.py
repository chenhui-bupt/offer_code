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

# graph = {1:[2, 3], 2:[], 3:[],  4:[5,6], 5:[], 6:[7], 7:[4]}
marked = dict(zip(graph.keys(), [False] * len(graph)))
onStack = dict(zip(graph.keys(), [False] * len(graph)))
cycles = []
edgeTo = dict(zip(graph.keys(), [-1] * len(graph)))
hasCycle = [False]
"""
6 2 5
2 1
3 1
5 2
5 3
6 5

"""

def dfs(graph, v, hasCycle):
    onStack[v] = True
    marked[v] = True
    for w in graph[v]:
        # if cycle:
        #     return
        if not marked[w]:  # 节点w不在marked里面，肯定就不在递归栈onStack里
            edgeTo[w] = v
            dfs(graph, w, hasCycle)
        elif onStack[w]:  # 节点w还在栈里，即上层的父节点还未执行完退出，而在本层递归又遇到，出现环路
            hasCycle[0] = True
    onStack[v] = False  # 执行完退出，栈标志为False

for v in graph:
    if not marked[v]:
        dfs(graph, v, hasCycle)
    if hasCycle[0]:
        print("hhh")
        exit()

marked = dict(zip(graph.keys(), [False] * len(graph)))
reversePost = []
def dfs2(graph, v):
    marked[v] = True
    for w in graph[v]:
        if not marked[w]:
            dfs2(graph, w)
    reversePost.append(v)

if not hasCycle[0]:
    for v in graph:
        if not marked[v]:
            dfs2(graph, v)
    print("拓扑排序是:",reversePost[::-1])

print()
new_graph = {}
for k, v in graph.items():
    for w in v:
        if w not in new_graph:
            new_graph[w] = []
        new_graph[w].append(k)
    if k not in new_graph:
        new_graph[k] = []
print(new_graph)
graph = new_graph

finished = dict(zip(graph.keys(), [False] * len(graph)))
workers = n
days = 0
i = 0
cando = []
reversePost = reversePost[::-1]
while i < len(reversePost):
    job = reversePost[i]
    print("正在处理job %d ...", job)
    flag = 1
    for yilai in graph[job]:
        if not finished[yilai]:
            print("job %d 依赖 job %d，无法被执行！" %(job, yilai))
            flag = 0
    if flag and workers > 0:
        print("job %d 能被执行，当前共有%d个工人可供使用" %(job, workers))
        cando.append(job)
        workers -= 1
    else:
        print("此次可被同时执行的job有:", cando)
        for can in cando:
            finished[can] = True
            print("\t job %d 执行完成" % can)
            workers += 1
        cando = []
        days += 1
        i -= 1
    i += 1
    print()
if cando:
    print("最后可被同时执行的job有:", cando)
    for can in cando:
        finished[can] = True
        workers += 1
    cando = []
    days += 1
print(days)



