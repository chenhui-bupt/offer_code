"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

"""
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        for j in range(len(intervals)):
            i = 0
            while i < len(intervals) - 1:
                if intervals[i].start > intervals[i+1].start:
                    intervals[i], intervals[i+1] = intervals[i+1], intervals[i]
                if intervals[i].end >= intervals[i+1].start:
                    if intervals[i].end < intervals[i+1].end:
                        intervals[i].end = intervals[i+1].end
                    intervals.remove(intervals[i+1])
                    i -= 1
                i += 1
            j += 1
        return intervals


s = Solution()
nums = [[1,3],[2,6],[8,10],[15,18]]
def result(nums):
    intervals = []
    for num in nums:
        intervals.append(Interval(num[0], num[1]))
    s.merge(intervals)
    res = []
    for interval in intervals:
        res.append([interval.start, interval.end])
    print(res)
result(nums)


# 使用优先队列
from queue import PriorityQueue

intervals = PriorityQueue()
for num in nums:
    intervals.put((num[0], Interval(num[0], num[1])))
res = []
head = intervals.get()
start, end = head[1].start, head[1].end
while intervals.qsize() > 0:
    interval = intervals.get()[1]
    if interval.start <= end:  # 有overlap
        end = max(interval.end, end)
    else:  # 没有overlap
        res.append(Interval(start, end))
        start = interval.start  # 更新start
        end = interval.end  # 更新end
res.append(Interval(start, end))
res1 = [[e.start, e.end] for e in res]
print(res1)


