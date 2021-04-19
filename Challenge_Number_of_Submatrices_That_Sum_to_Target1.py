# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 17:09:00 2021

@author: ppj
"""

matrix = [[0,1,0],[1,1,1],[0,1,0],[0,1,0]]
target = 0

m=len(matrix)
n=len(matrix[0])

#rec=[[None]*n for i in range(m)]
rec=matrix.copy()

for i in range(m):
    for j in range(n):
        print('i',i)
        print(j)
        if i==j==0:
            continue
        if i==0:
            rec[i][j]=rec[i][j-1]+matrix[i][j]
            continue
        if j==0:
            rec[i][j]=rec[i-1][j]+matrix[i][j]
            continue
        rec[i][j]=matrix[i][j]+rec[i-1][j]+rec[i][j-1]-rec[i-1][j-1]
        
        
print(rec)
        
#%%
import collections
matrix = [[0,1,0],[1,1,1],[0,1,0],[0,1,0]]

A=matrix
m, n = len(A), len(A[0])
for row in A:
    for i in range(n - 1):
        row[i + 1] += row[i]

res = 0
for i in range(n):
    for j in range(i, n):
        c = collections.defaultdict(int)
        cur, c[0] = 0, 1
        for k in range(m):
            cur += A[k][j] - (A[k][i - 1] if i > 0 else 0)
            res += c[cur - target]
            c[cur] += 1
print(res)