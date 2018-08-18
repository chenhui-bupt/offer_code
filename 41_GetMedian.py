# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.left = []
        self.right = []
        self.count = 0
    def Insert(self, num):
        if self.count % 2 == 0: # 偶数时（为确保即将加入最小堆的num，比最大堆中的最大值还要大，
        # 因此，先加入最大堆，调整最大堆，将最大值弹出加入最小堆即可，保证最小堆始终大于最大堆中的值。
            self.left.append(num)
            self.maxHeap(self.left)
            maxNum = self.left.pop(0)
            self.right.append(maxNum) # 最小堆
        else:
            self.right.append(num)
            self.minHeap(self.right)
            minNum = self.right.pop(0)
            self.left.append(minNum) # 最大堆
        self.maxHeap(self.left) # 最大堆调整
        self.minHeap(self.right) # 最小堆调整
        self.count += 1

    def GetMedian(self):
        if self.count == 1:
            return self.right[0] # 最小堆
        if self.count % 2 == 0:
            return (self.left[0] + self.right[0])/2.0
        else:
            return self.right[0] # 最小堆
        
    def maxHeap(self, arr):
        if not arr:
            return []
        length = len(arr)
        if length == 1:
            return arr
        end = length - 1
        for i in range(length//2, -1, -1):
            start = i
            startVal = arr[i]
            child = start * 2 + 1
            while(child <= end):
                if child < end and arr[child] < arr[child + 1]:
                    child += 1
                if arr[start] >= arr[child]:
                    break
                arr[start] = arr[child] # 子节点上移，根节点下滑
                start = child
                child = child * 2 + 1
            arr[start] = startVal # 根节点下滑
            
    def minHeap(self, arr):
        if not arr:
            return []
        length = len(arr)
        if length == 1:
            return arr
        end = length - 1
        for i in range(length//2, -1, -1):
            start = i
            startVal = arr[i]
            child = start *2 + 1
            while(child <= end):
                if child < end and arr[child] > arr[child + 1]:
                    child += 1
                if arr[start] <= arr[child]:
                    break
                arr[start] = arr[child] # 子节点上移，根节点下滑
                start = child
                child = child * 2 + 1
            arr[start] = startVal # 根节点下滑
    
    


s = Solution()
s.Insert(5)
print(s.GetMedian())
s.Insert(2)
print(s.GetMedian())
s.Insert(3)
print(s.GetMedian())

del s
s = Solution()
s.Insert(5)
s.Insert(2)
s.Insert(3)
s.Insert(4)
s.Insert(1)
s.Insert(6)
s.Insert(7)
s.Insert(0)
s.Insert(8)
print(s.GetMedian())
