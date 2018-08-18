# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return
        rows = len(matrix)
        columns = len(matrix[0])
        start = 0
        printArray = []
        while(columns > start * 2 and rows > start * 2): # 因为一圈一圈的打印，所以必须满足此条件
            printArray = printArray + self.printMatrixInCircle(matrix, columns, rows, start)
            start += 1
        return printArray
    
    def printMatrixInCircle(self, matrix, columns, rows, start):
        endX = columns - 1 - start
        endY = rows - 1 -start
        printArray = []
        # 从左到右打印一行
        for j in range(start, endX + 1):
            number = matrix[start][j]
            printArray.append(number)
        # 从上到下打印一行， 至少要有两行
        if start < endY: # 至少要有两行
            for i in range(start + 1, endY + 1):
                number = matrix[i][endX]
                printArray.append(number)
        # 从右到左打印一列, 至少要有两行两列
        if start < endY and start < endX:
            for j in range(endX - 1, start - 1, -1):
                number = matrix[endY][j]
                printArray.append(number)
        # 从下到上打印一列, 要有三行
        if start < endY - 1 and start < endX:
            for i in range(endY - 1, start, -1):
                number = matrix[i][start]
                printArray.append(number)
        return printArray
    



    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return
        printArray = []
        while(matrix):
            printArray += matrix.pop(0) # 第一行打印出去
            if not matrix:
                break
            matrix = self.turnMatrix(matrix)
        return printArray

    def turnMatrix(self, matrix): # 逆时针旋转
        rows = len(matrix)
        cols = len(matrix[0])
        turnedMat = []
        for j in range(cols-1, -1, -1):
            turnedList = []
            for i in range(rows):
                turnedList.append(matrix[i][j])
            turnedMat.append(turnedList)
        return turnedMat

    def printMatrix(self, matrix):
        # write code here
        if not matrix:
            return
        minI = 0
        maxI = len(matrix) - 1
        minJ = 0
        maxJ = len(matrix[0]) - 1
        i = 0
        j = 0
        printList = []
        while minI <= maxI and minJ <= maxJ:
            for j in range(minJ, maxJ + 1):
                printList.append(matrix[i][j])
            minI += 1
            if minJ <= maxJ:
                for i in range(minI, maxI + 1):
                    printList.append(matrix[i][j])
                maxJ -= 1
            if minI <= maxI:
                for j in range(maxJ, minJ - 1, -1):
                    printList.append(matrix[i][j])
                maxI -= 1
            if minJ <= maxJ:
                for i in range(maxI, minI - 1, -1):
                    printList.append(matrix[i][j])
                minJ += 1
        return printList





