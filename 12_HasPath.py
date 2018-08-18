# -*- coding:utf-8 -*-
# 面试题12： 矩阵中的路径

class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        if matrix==None or rows<1 or cols<1 or path==None:
            return False
        visted=[0]*(cols*rows)
        pathLength=0
        for row in range(rows):
            for col in range(cols):
                if(self.hasPathCore(matrix,rows,cols,path,row,col,pathLength,visted)):
                    return True
        return False
    def hasPathCore(self,matrix,rows,cols,path,row,col,pathLength,visited):
        if pathLength==len(path):
            return True #重要，说明路径寻找完毕，返回True
        hasPath=False
        if(rows>row>=0)and(cols>col>=0)and(not visited[row*cols+col])and\
        (matrix[row*cols+col]==path[pathLength]):
            pathLength+=1
            visited[row*cols+col]=True
            hasPath=self.hasPathCore(matrix,rows,cols,path,row-1,col,pathLength,visited) or \
            self.hasPathCore(matrix,rows,cols,path,row+1,col,pathLength,visited) or\
            self.hasPathCore(matrix,rows,cols,path,row,col-1,pathLength,visited) or\
            self.hasPathCore(matrix,rows,cols,path,row,col+1,pathLength,visited)
            if not hasPath: #回溯
                pathLength-=1
                visited[row*cols+col]=False
        return hasPath
        