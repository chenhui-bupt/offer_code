# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        # write code here
        if not data:
            return
        # return self.helper(data)
        return self.msort(data, 0, len(data) - 1)%1000000007

    def msort(self, arr, left, right):
        if left >= right:
            return 0
        mid = (left + right) // 2
        leftCnt = self.msort(arr, left, mid)%1000000007
        rightCnt = self.msort(arr, mid + 1, right)%1000000007
        mergeCnt = self.merge(arr, left, mid, right)%1000000007
        return (leftCnt + rightCnt + mergeCnt)%1000000007

    def merge(self, arr, left, mid, right):
        cnt = 0
        temp = []
        i = left
        j = mid + 1
        while i <= mid and j <= right:
            if arr[i] < arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
                cnt += (mid + 1 - i)
        temp += arr[i: mid + 1]
        temp += arr[j: right + 1]
        arr[left: right + 1] = temp
        return cnt

    def helper(self, arr):
        if not arr:
            return 0
        copy = sorted(arr)
        cnt = 0
        for i in range(len(copy)):
            cnt += (arr.index(copy[i]))%1000000007
            arr.remove(copy[i])
        return cnt%1000000007


s = Solution()
import datetime
start = datetime.datetime.now()
print(s.InversePairs([364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]))
end = datetime.datetime.now()
print(end-start)
print(s.InversePairs([1, 2, 3, 4, 5, 6, 7, 0]))
