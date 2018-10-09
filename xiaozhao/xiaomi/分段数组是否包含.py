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
"""
3
1 2 3
2 5 6
8
"""
n = int(input())
nums = []
for i in range(n):
    nums.append(list(map(int, input().split())))
#print(nums)
from queue import PriorityQueue
pq = PriorityQueue()
for num in nums:
    pq.put(num)
res = []
tSet = pq.get()
while pq.qsize() > 0:
    tmp = pq.get()
    if tmp[0] <= tSet[-1]:  # 有overlap(后面的分段的start的小于前面分段的end
        tSet = list(set(tSet + tmp))
    else:  # 没有overlap
        res.append(tSet[::])  # 没有overlap才能追加至返回列表中
        tSet = tmp[::]
res.append(tSet)  # 最后一个分段也要加入
#print(res)
print(len(res))
print(max(map(len, res)))
