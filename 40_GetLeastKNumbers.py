# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution0(self, tinput, k):
        # write code here
        if not tinput or k <= 0 or k > len(tinput):
            return []
        start = 0
        end = len(tinput) - 1
        index = self.Partition(tinput, start, end)
        while(index != k-1):
            if index > k - 1:
                end = index - 1
                index = self.Partition(tinput, start, end)
            else:
                start = index + 1
                index = self.Partition(tinput, start, end)
        return sorted(tinput[:k])
        
    def Partition(self, arr, left, right):
        pivotKey = arr[left]
        while(left < right):
            while(left < right and arr[right] >= pivotKey): # right指针找到比基准小的元素
                right -= 1
            arr[left] = arr[right] # 移到左边
            while(left < right and arr[left] <= pivotKey): # left指针找到比基准大的元素
                left += 1
            arr[right] = arr[left]
        arr[left] = pivotKey # 把基准移到中间
        return left
    
    
    def HeapAdjust(self, arr, start, end):
        temp = arr[start]
        child = start * 2 + 1
        while child <= end:
            if child < end and arr[child] < arr[child + 1]:
                child += 1
            if arr[child] <= temp: # 已是最大堆，break
                break
            arr[start] = arr[child]
            start = child
            child = child * 2 + 1
        arr[start] = temp #插入
    
    def HeapSort(self, arr):
        if not arr:
            return
        # 建立大顶堆
        for i in range(len(arr)//2, -1, -1):
            self.HeapAdjust(arr, i, len(arr) - 1)
        # 调整堆
        for i in range(len(arr) - 1, -1, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.HeapAdjust(arr, 0, i - 1)
    
    def GetLeastNumbers_Solution(self, tinput, k):
        if not tinput or k <= 0 or k > len(tinput):
            return []
        kContainer = []
        for num in tinput:
            if len(kContainer) < k:
                kContainer.append(num)
            else:
                for i in range(k//2, -1, -1):
                    self.HeapAdjust(kContainer, i, k-1)
                if num >= kContainer[0]:
                    continue
                else:
                    kContainer[0] = num
        self.HeapSort(kContainer)
        return kContainer
    