"""
完全多部图，同一集合内任意两点没有边相连，不同集合间任意两点均有边相连
1 3
1 5
2 3
2 5
3 4
4 5
3 5"""
graph = {1:[3,5], 2:[3,5], 3:[1, 2, 4, 5], 4:[3, 5], 5:[1, 2, 3, 4]}
nodes = list(range(1, 6))

def isMultiPartite(graph):
    marked = dict(zip(nodes, [False] * len(nodes)))
    isMultiPartite = True
    for node in nodes:
        if not marked[node]:
            marked[node] = True
            oneSide = graph[node]
            otherSide = [other for other in nodes if other not in oneSide]
            for other in otherSide:
                marked[other] = True
                if set(oneSide) != set(graph[other]):
                    isMultiPartite = False
                    break
        if not isMultiPartite:
            break
    return isMultiPartite
print(isMultiPartite(graph))

graph = {1:[2], 2:[1, 3], 3:[2, 4], 4:[]}
nodes = list(range(1, 5))
print(isMultiPartite(graph))





