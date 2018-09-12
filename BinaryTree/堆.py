"""实现堆的构建，排序，插入，以及删除根节点
大顶堆
"""


class heap:
    def __init__(self, nums):
        self.nums = nums
        self.heapCreate()

    def heapAdjust(self, start, end):
        temp = self.nums[start]
        child = start * 2 + 1
        while child <= end:
            if child < end and self.nums[child] < self.nums[child + 1]:
                child += 1
            if temp >= self.nums[child]:
                break
            self.nums[start] = self.nums[child]
            start = child
            child = start * 2 + 1
        self.nums[start] = temp

    def heapCreate(self):
        for i in range(len(self.nums)//2, -1, -1):
            self.heapAdjust(i, len(self.nums) - 1)

    def insert(self, node):
        self.nums.append(node)
        child = len(self.nums) - 1
        start = (child - 1) // 2
        while start >= 0 and node > self.nums[start]:
            self.nums[child] = self.nums[start]
            child = start
            start = (child - 1) // 2
        self.nums[child] = node

    def deleteMin(self):
        self.nums[0] = self.nums[-1]
        self.nums.pop()
        self.heapAdjust(0, len(self.nums) - 1)

    def heapSort(self):
        for i in range(len(self.nums) - 1, -1, -1):
            self.nums[0], self.nums[i] = self.nums[i], self.nums[0]
            self.heapAdjust(0, i - 1)  # 注意是i-1


nums = [9,3,7,6,5,1,10,2]
h = heap(nums)
# print(h.nums)
# h.heapSort()
print(h.nums)
h.insert(1.5)
print(h.nums)
h.deleteMin()
print(h.nums)

nums = [52, 32, 73, 23, 42, 62, 99, 14, 24, 39,43, 58,65, 80,120]
h = heap(nums)
print(h.nums)



