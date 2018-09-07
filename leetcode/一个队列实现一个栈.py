"""
225. Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/description/
"""
class Solution:
    def __init__(self):
        self.queue = []

    def push(self, node):
        self.queue.append(node)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            return None

    def top(self):
        if self.queue:
            return self.queue[0]
        else:
            return None

    def empty(self):
        return len(self.queue) == 0

