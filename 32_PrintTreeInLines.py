# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def printTreeInLine(self, root):
        if not root:
            return
        queue = []  # 宽度优先搜索，用队列
        queue.append(root)
        printTree = []
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.pop(0)
                printTree.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            print(printTree)
            printTree = []

    def printTreeInLine2(self, root):
        if not root:
            return
        queue = []
        queue.append(root)
        printTree = []
        nextLevel = 0
        toBePrinted = 1  # 初始根节点第一层只有一个节点
        while(queue):
            pNode = queue.pop(0)
            printTree.append(pNode.val)
            if pNode.left:
                queue.append(pNode.left)
                nextLevel += 1
            if pNode.right:
                queue.append(pNode.right)
                nextLevel += 1
            toBePrinted -= 1
            if toBePrinted == 0:
                print(printTree)
                printTree = []
                toBePrinted = nextLevel
                nextLevel = 0


pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

s = Solution()
s.printTreeInLine(pNode1)
s.printTreeInLine2(pNode1)
