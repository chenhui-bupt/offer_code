class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def search(root, value, res):
    if not root:
        return False
    elif root.val == value:
        res[0] = root
        return True
    elif root.val < value:
        return search(root.right, value, res)
    else:
        return search(root.left, value, res)

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

"""
在二叉查找树删去一个结点，分三种情况讨论：

若*p结点为叶子结点，即PL（左子树）和PR（右子树）均为空树。由于删去叶子结点不破坏整棵树的结构，则只需修改其双亲结点的指针即可。
若*p结点只有左子树PL或右子树PR，此时只要令PL或PR直接成为其双亲结点*f的左子树（当*p是左子树）或右子树（当*p是右子树）即可，作此修改也不破坏二叉查找树的特性。
若*p结点的左子树和右子树均不空。在删去*p之后，为保持其它元素之间的相对位置不变，可按中序遍历保持有序进行调整，可以有两种做法：其一是令*p的左子树为*f的左/右（依*p是*f的左子树还是右子树而定）子树，*s为*p左子树的最右下的结点，而*p的右子树为*s的右子树；其二是令*p的直接前驱（in-order predecessor）或直接后继（in-order successor）替代*p，然后再从二叉查找树中删去它的直接前驱（或直接后继）。
"""
def delete(root, value):
    if not root:
        return None
    else:
        if value == root.val:
            root = deleteNode(root)
        elif value < root.val:
            root.left = delete(root.left, value)
        else:
            root.right = delete(root.right, value)
        return root

def deleteNode(p):
    if not p.left and not p.right:  # 叶子节点
        del p  # 直接删除
        p = None
    elif not p.right:  # 只有左子树
        p = p.left  # 直接删除，左子节点上移
    elif not p.left:  # 只有右子树
        p = p.right  # 直接删除，右子节点上移
    else:  # 左右子树都有
        q = p
        s = p.left
        while s.right:
            q = s  # 记录s的父亲节点（重要）
            s = s.right  # s为左子树的最右节点（即小于p的最大节点）
        p.val = s.val  # 将s的值复制到p上
        if q != p:  # 上面while语句被执行，s为p的左子树的最右子节点
            q.right = s.left  # 把s的左子树给其父亲的右节点（因为s上移复制到p上，所以s得左子树，顶上s的位置作为s父亲q的右子树）
        else:  # while没被执行，s为p的左子树
            q.left = s.left  # 重接q的左子树（因为s为p的左子节点需要上移，且s只有左子树，左子树也跟着上移就行）
        del s
    return p
            


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


print("search...")
res = [None]
print(search(node8, 14, res))
if res[0]:
    print(res[0].val)

print("insert...")
insert(node8, 9)
res = inOrder(node8)
print(res)

print("delete...")
delete(node8, 3)
res = inOrder(node8)
print(res)

