list1 = [[1, 10], [8, 15], [20, 30]]
list2 = [[2, 12], [22, 25]]

from queue import PriorityQueue
def cleanOverlap(nums):
    pq = PriorityQueue()
    for num in nums:
        pq.put(num)
    res = []
    start, end = pq.get()
    while pq.qsize() > 0:
        num = pq.get()
        if num[0] <= end:  # 有overlap(后面的分段的start的小于前面分段的end
            end = max(end, num[1])
        else:  # 没有overlap
            res.append([start, end])  # 没有overlap才能追加至返回列表中
            start = num[0]  # 更新start
            end = num[1]  # 更新end
    res.append([start, end])  # 最后一个分段也要加入
    return res

list1 = cleanOverlap(list1)
list2 = cleanOverlap(list2)
print(list1, list2)


def isCompleteOverlap(nums1, nums2):  # 判断nums2是否包含于nums1
    nums1 = cleanOverlap(nums1)
    nums2 = cleanOverlap(nums2)
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i][0] <= nums2[j][0] and nums2[j][1] <= nums1[i][1]:
            j += 1
        else:
            i += 1
    return j == len(nums2)


res = isCompleteOverlap(list1, list2)
print(res)
list1 = [[1, 10], [8, 15], [20, 30]]
list2 = [[2, 12], [18, 25]]
res = isCompleteOverlap(list1, list2)
print(res)