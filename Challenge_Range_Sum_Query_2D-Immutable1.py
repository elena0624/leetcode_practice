# -*- coding: utf-8 -*-
"""
Created on Wed May 12 17:57:42 2021

@author: ppj
"""

NumMatrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
sumRegion = [2, 1, 4, 3]
sumRegion = [1, 1, 2, 2]
sumRegion = [1, 2, 2, 4]

#SumMatrix = [x[:] for x in NumMatrix]
SumMatrix = [[0 for i in range(len(NumMatrix[0])+1)] for i in range(len(NumMatrix)+1)]

for i in range(1,len(NumMatrix)+1):
    for j in range(1,len(NumMatrix[0])+1):
#        print(i,j,SumMatrix[i-1][j]+SumMatrix[i][j-1]+NumMatrix[i-1][j-1]-SumMatrix[i-1][j-1])
        SumMatrix[i][j] = SumMatrix[i-1][j]+SumMatrix[i][j-1]+NumMatrix[i-1][j-1]-SumMatrix[i-1][j-1]
print(SumMatrix[sumRegion[2]+1][sumRegion[3]+1]-SumMatrix[sumRegion[0]][sumRegion[3]+1]-SumMatrix[sumRegion[2]+1][sumRegion[1]]+SumMatrix[sumRegion[0]][sumRegion[1]])