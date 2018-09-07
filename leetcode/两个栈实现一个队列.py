
"""
232. Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/description/
"""
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2.pop()
        else:
            return None

    def top(self):
        if self.stack2:
            return self.stack2[-1]
        elif self.stack1:
            return self.stack1[0]
        else:
            return None

    def empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0
