graph = {8:[6, 10], }

class GraphNode(object):
    def __init__(self, val):
        self.val = val
        self.neighbors = []


# 假设图中各节点的值不一样
visited = dict()
def DeepCopy(pGraphNode):
    if not pGraphNode:
        return None
    if id(pGraphNode) not in visited:
        root = GraphNode(pGraphNode.val)
        visited[id(pGraphNode)] = root
        for pNode in pGraphNode.neighbors:
            root.neighbors.append(DeepCopy(pNode))
        return root
    else:
        return visited[id(pGraphNode)]






