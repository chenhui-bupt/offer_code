# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def printTreeInZigzag(self, root):
        if not root:
            return
        queue = []
        queue.append(root)
        printTree = []
        nextLevel = 0
        toBePrinted = 1
        zigzag = 1
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
                if zigzag % 2:
                    print(printTree)
                else:
                    print(printTree[::-1])
                zigzag += 1
                printTree = []
                toBePrinted = nextLevel
                nextLevel = 0

    def printTreesInZigzag2(self, root):
        if not root:
            return
        levels = [[], []]
        current = 0
        next = 1
        levels[0].append(root)
        while(len(levels[0])>0 or len(levels[1])>0):
            pNode = levels[current].pop()
            print(pNode.val, end=' ')
            if current == 0:  # 当前是从左往右打印，下一层应该从右往左
                if pNode.left:  # 先压入左子树入栈
                    levels[next].append(pNode.left)
                if pNode.right:
                    levels[next].append(pNode.right)
            else:  # 当前是从右往左，下一层是从左往右
                if pNode.right:  # 先压入右子树入栈
                    levels[next].append(pNode.right)
                if pNode.left:
                    levels[next].append(pNode.left)
            if(len(levels[current]) == 0):  # 反转
                print('\n')            
                current = 1 - current  # 反转
                next = 1 - next




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
s.printTreesInZigzag2(pNode1)
