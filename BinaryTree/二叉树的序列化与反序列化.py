"""
https://www.cnblogs.com/linyx/p/4066019.html
https://www.geeksforgeeks.org/serialize-deserialize-binary-tree/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def serialize(root, res):
    if not root:
        return
    res.append(root.val)
    if root.left:
        serialize(root.left, res)
    if root.right:
        serialize(root.right, res)
    res.append('#')

def deserialize(data):
    ch = data.pop(0)
    if ch == '#':
        return
    root = TreeNode(ch)
    left = deserialize(data)
    if left:
        root.left = left
        right = deserialize(data)
        if right:
            root.right = right
    return root

pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode3.left = pNode5
pNode3.right = pNode6

def preOrder(root, res):
    if root:
        res.append(root.val)
        preOrder(root.left, res)
        preOrder(root.right, res)

s = []
serialize(pNode1, s)
print(''.join(map(str, s)))
root = deserialize(s)
res = []
preOrder(root, res)
print(''.join(map(str,res)))
