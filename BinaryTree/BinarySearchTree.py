class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def searchBST(root, value, res):
    if not root:
        return False
    elif root.val == value:
        res[0] = root
        return True
    elif root.val < value:
        return searchBST(root.right, value, res)
    else:
        return searchBST(root.left, value, res)

def insert(root, value):
    if not root:
        root = TreeNode(value)
        return root
    if root.val == value:
        return root  # 插入失败
    elif value < root.val:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root  # 插入成功

node8 = TreeNode(8)
node3 = TreeNode(3)
node10 = TreeNode(10)
node1 = TreeNode(1)
node6 = TreeNode(6)
node14 = TreeNode(14)
node4 = TreeNode(4)
node7 = TreeNode(7)
node13 = TreeNode(13)
node8.left = node3
node8.right = node10
node3.left = node1
node3.right = node6
node10.right = node14
node6.left = node4
node6.right = node7
node14.left = node13

res = [None]
print(searchBST(node8, 14, res))
if res[0]:
    print(res[0].val)

def inOrder(root):
    if not root:
        return []
    res = []
    stack = [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res
insert(node8, 9)
res = inOrder(node8)
print(res)

insert(node8, 3)
res = inOrder(node8)
print(res)

