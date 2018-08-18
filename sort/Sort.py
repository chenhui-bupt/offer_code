#-*-coding:utf-8-*-
class Solution:
    # 冒泡排序从小到大排序
    def BubbleSort(self, arr): # O(n^2)
        if not arr:
            return
        for i in range(len(arr)):
            for j in range(0, len(arr)-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr  # 可有可无

    # 冒泡排序，通过相邻元素的比较交换，每次把最小的元素一步一步的移到正确位置上
    def BubbleSort2(self, arr):  # O(nlogn)
        if not arr:
            return
        for i in range(0, len(arr)):
            for j in range(len(arr)-1, i, -1): # 冒泡嘛，要把最小的一步一步冒上去
                if arr[j] < arr[j-1]:
                    arr[j-1], arr[j] = arr[j], arr[j-1]
        return arr # 可有可无

    # 选择排序，每次选择未排序中最小的元素，直接放在正确位置上
    def SelectSort(self, arr):  # O(nlogn)
        if not arr:
            return
        for i in range(len(arr) - 1):
            minIndex = i
            for j in range(i + 1, len(arr)):  # 从i+1 开始比
                if arr[j] < arr[minIndex]:
                    minIndex = j  # 找到未排序中最小的元素对应的下标
            if minIndex != i:
                arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr  # 可有可无

    # 假定第一位排序正确，第二位开始往前找只要前面的数字比目标值大就往后移位，
    # 直到目标值不在小于当前位置，或者出界，就把目标值插入到当前位置
    # 他与选择排序的区别是，选择排序每次都找到最小的放到正确的位置上，（过程中能保证头部有序）
    # 而插入是只要小就往前插，大的数还要往后顺移（过程中只能保证局部有序）
    def InsertSort(self, arr):
        if not arr:
            return
        for i in range(1, len(arr)):
            j = i
            target = arr[i]  # 待被插入的目标
            while(j > 0 and target < arr[j - 1]):  # 大于目标值, 对比值后移直到不再大于目标值，给目标值挪动移出一个空位
                arr[j] = arr[j - 1]  # 后移，移出空位
                j -= 1
            arr[j] = target  # 插入
        return arr  # 可有可无


    
    # 快速排序，递归思想，以数组第一个元素为基准，把比他小的移到左边，比他大的移到右边，返回基准值新的下表，然后对左右两边递归调用，即可完成排序
    def partition0(self, arr, left, right): # O(nlogn)
        pivotKey = arr[left]
        pivotPointer = left
        while(left < right):
            while(left < right and arr[right] >= pivotKey): # 找到比基准pivotKey小的元素
                right -= 1
            while(left < right and arr[left] <= pivotKey): # 找到比基准pivotKey大的元素
                left += 1
            arr[left], arr[right] = arr[right], arr[left] # 大的交换的右边，小的交换到左边
        arr[pivotPointer], arr[left] = arr[left], arr[pivotPointer] # 把pivotKey交换到中间
        return left # 返回中间下标 

    def partition(self, arr, left, right):
        pivotKey = arr[left]
        while(left < right):
            while(left < right and arr[right] >= pivotKey): # 找到比基准pivotKey小的元素
                right -= 1
            arr[left] = arr[right] # 把小的移到左边
            while(left < right and arr[left] <= pivotKey):
                left += 1
            arr[right] = arr[left] # 把大的移到右边
        arr[left] = pivotKey # 最后把pivotKey赋值到中间
        return left

    def QuickSort(self, arr):
        if not arr:
            return
        return self.QuickSortHelper(arr, 0 , len(arr)-1)

    def QuickSortHelper(self, arr, left, right):
        if left >= right:
            return
        pivotPointer = self.partition(arr, left, right)
        self.QuickSortHelper(arr, left, pivotPointer - 1)
        self.QuickSortHelper(arr, pivotPointer + 1, right)
        return arr  # 可有可无


    # 堆排序
    def HeapAdjust(self, arr, start, end):
        temp = arr[start]
        i = 2 * start + 1  # 左右孩子的节点分别是2i+1，2i+2
        while(i <= end):
            if(i < end and arr[i] < arr[i + 1]):
                i += 1
            if(temp >= arr[i]):  # 已经是大顶堆，保持
                break
            arr[start] = arr[i]  # 将子节点上移
            start = i  # 下一轮筛选
            i = 2 * i + 1  # i到子层
        arr[start] = temp  # 插入正确的位置

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

    def MergeSort(self, arr):
        if not arr:
            return
        self.msort(arr, 0, len(arr) - 1)
        return arr

    def msort(self, arr, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        self.msort(arr, left, mid)
        self.msort(arr, mid + 1, right)
        self.merge(arr, left, mid, right)

    def merge(self, arr, left, mid, right):
        temp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        while i <= mid:
            temp.append(arr[i])
            i += 1
        while j <= right:
            temp.append(arr[j])
            j += 1
        for k in range(len(temp)):
            arr[left + k] = temp[k]









s = Solution()
arr0 = [9,2,1,7,6,8,5,3,4]

res = arr0[::]
s.BubbleSort(res)
print("冒泡排序", res)

res = arr0[::]
s.BubbleSort2(res)
print("冒泡排序", res)

res = arr0[::]
s.SelectSort(res)
print("选择排序", res)

res = arr0[::]
s.InsertSort(res)
print("插入排序", res)

res = arr0[::]
s.QuickSort(res)
print("快速排序", res)

res = arr0[::]
s.HeapSort(res)
print("堆排序", res)

res = arr0[::]
s.MergeSort(res)
print("归并排序", res)

