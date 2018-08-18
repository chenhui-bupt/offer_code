#!/usr/bin/env python
#-*-coding:utf-8-*-

def heap_sort(lst):
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            print(lst)
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]: # 最大堆调整（调整start节点小的话，就滑至较大的子节点）
                lst[root], lst[child] = lst[child], lst[root] # 父子节点交换
                root = child # 到子层 （将子节点作为新的根节点，继续调整，直到滑至不需要交换，或者越界为止
            else:
                break # 父节点大于子节点，则break

    # 创建最大堆
    for start in range((len(lst) - 2) // 2, -1, -1):
        sift_down(start, len(lst) - 1)

    # 堆排序
    for end in range(len(lst) - 1, 0, -1): # 从后往前，因为每次堆都会找出一个最大节点，并移除（其实是放到列表末尾），实现选择排序
        lst[0], lst[end] = lst[end], lst[0] # 交换根节点至最后，一次for循环都把最后一个节点移除（下次不再考虑）
        sift_down(0, end - 1) # 重新调整节点变成最大堆，待下次选择排序
    return lst
            
def main():
    l = [9,2,1,7,6,8,5,3,4]
    l = [1,3,2,4,5]
    res = heap_sort(l)
    print(res)

if __name__ == "__main__":
    main()