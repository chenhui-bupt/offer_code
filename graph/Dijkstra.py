def dijkstra(graph, v):
    priority_queue.insert(s, 0.0)
    while priority_queue:





graph = {0: {2: 0.26, 4: 0.28}, 1: {3: 0.29}, 2: {7: .34}, 3: {6: .52}, 4: {7: .37, 5: .35},
         5: {1: .32, 7: .28, 4: .35}, 6: {4: .93, 0: .58, 2: .40}, 7: {3: .39, 5: .28}}
s = 0
distTo = [0xffffffff] * len(graph)
distTo[s] = 0
edgeTo = [-1] * len(graph)
priority_queue = []
