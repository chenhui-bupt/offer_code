

def dfs(graph, v):
    pre.append(v)
    marked[v] = True
    for w in graph[v]:
        if not marked[w]:
            dfs(graph, w)
    post.append(v)
    reversePost.append(v)

graph = {0: [1, 5], 1: [], 2: [0, 3], 3: [2, 5], 4: [2, 3], 5: [4]}
marked = [False] * len(graph)
pre = []
post = []
reversePost = []
for v in graph:
    if not marked[v]:
        dfs(graph, v)
print(pre)
print(post)
print(reversePost)

