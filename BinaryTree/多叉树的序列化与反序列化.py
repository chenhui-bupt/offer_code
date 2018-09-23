"""
https://www.geeksforgeeks.org/serialize-deserialize-n-ary-tree/
"""
N = 5
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.children = []


def serialize(root, res):
    if not root:
        return
    res.append(str(root.val))
    for child in root.children:
        serialize(child, res)
    res.append('#')


def deserialize(data):
    num = data.pop(0)
    if num == '#':
        return None
    else:
        root = TreeNode(num)
        child = deserialize(data)
        while child:
            root.children.append(child)
            child = deserialize(data)
        return root


A = TreeNode('A')
B = TreeNode('B')
C = TreeNode('C')
D = TreeNode('D')
E = TreeNode('E')
F = TreeNode('F')
G = TreeNode('G')
H = TreeNode('H')
I = TreeNode('I')
J = TreeNode('J')
K = TreeNode('K')
A.children = [B, C, D]
B.children = [E, F]
D.children = [G, H, I, J]
F.children = [K]

s = []
serialize(A, s)
print(''.join(s))

root = deserialize(s)
def preOrder(root, res):
    if root:
        res.append(root.val)
        for child in root.children:
            preOrder(child, res)
res = []
preOrder(root, res)
print(''.join(res))