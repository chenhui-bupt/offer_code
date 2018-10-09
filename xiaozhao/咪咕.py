def printMatrix(matrix):
    # write code here
    if not matrix:
        return
    printArray = []
    while (matrix):
        printArray += matrix.pop(0)  # 第一行打印出去
        if not matrix:
            break
        matrix = turnMatrix(matrix)
    return printArray


def turnMatrix(matrix):  # 逆时针旋转
    rows = len(matrix)
    cols = len(matrix[0])
    turnedMat = []
    for j in range(cols - 1, -1, -1):
        turnedList = []
        for i in range(rows):
            turnedList.append(matrix[i][j])
        turnedMat.append(turnedList)
    return turnedMat
"""
3
3
1 2 3 4 5 6 7 8 9
"""


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
m = int(input())
n = int(input())
nums = input().split()
mat = []
for i in range(m):
    mat.append(nums[i*n: i*n + n])
res = printMatrix(mat)
print('\n'.join(res))

