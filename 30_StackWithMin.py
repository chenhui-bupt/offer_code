# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.m_data = []
        self.m_min = []
        
    def push(self, node):
        # write code here
        self.m_data.append(node)
        if self.m_min:
            if node < self.m_min[-1]:
                self.m_min.append(node)
            else:
                self.m_min.append(self.m_min[-1])
        else:
            self.m_min.append(node)
            
    def pop(self):
        # write code here
        node = self.m_data.pop()
        self.m_min.pop()
        return node
    
    def top(self):
        # write code here
        return self.m_data[-1]
    
    def min(self):
        # write code here
        if self.m_min:
            return self.m_min[-1]
        return None
    