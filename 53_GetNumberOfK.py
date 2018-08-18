# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        if not data or not k:
            return 0
        left = 0
        right = len(data) - 1
        first = self.getFirstK(data, k, left, right)
        last = self.getLastK(data, k, left, right)
        if first > -1 and last > -1:
            return last - first + 1
        else:
            return 0

    def getFirstK(self, data, k, left, right):
        while left <= right:
            mid = (left + right) >> 1
            if data[mid] > k:
                right = mid - 1
            elif data[mid] < k:
                left = mid + 1
            elif mid >= 1 and data[mid - 1] == k:
                right = mid - 1
            else:
                return mid
        return -1

    def getLastK(self, data, k, left, right):
        while left <= right:
            mid = (left + right) >> 1
            if data[mid] < k:
                left = mid + 1
            elif data[mid] > k:
                right = mid - 1
            elif mid < len(data) - 1 and data[mid + 1] == k:
                left = mid + 1
            else:
                return mid
        return -1








"""
不正确版本
"""
class Solution:
    def GetNumberOfK(self, data, k):
        if not data or not k:
            return 0
        left = 0
        right = len(data) - 1
        first = self.getFirstK2(data, k, left, right)
        last = self.getLastK2(data, k, left, right)
        if first == -1:
            return 0
        else:
            return last - first + 1

    def getFirstK(self, data, k, left, right):
        if left == right:
            return left
        if left > right:
            return -1
        mid = (left + right) >> 1
        if data[mid] >= k:
            return self.getFirstK(data, k, left, mid)
        else:
            return self.getFirstK(data, k, mid + 1, right)

    def getFirstK2(self, data, k, left, right):
        while left <= right:
            if left == right:
                return left
            mid = (left + right) >> 1
            if data[mid] >= k:
                right = mid
            else:
                left = mid + 1
        return -1

    def getLastK(self, data, k, left, right):
        if left == right:
            return right
        if left > right:
            return -1
        mid = (left + right) >> 1
        if data[mid] <= k:
            return self.getLastK(data, k, mid, right)
        else:
            return self.getLastK(data, k, left, mid - 1)

    def getLastK2(self, data, k, left, right):
        while left <= right:
            if left == right:
                return right
            mid = (left + right) >> 1
            if data[mid] <= k:
                left = mid
            else:
                right = mid - 1
        return -1