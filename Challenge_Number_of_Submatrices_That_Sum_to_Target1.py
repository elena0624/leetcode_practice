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
# 以上是計算所有右下角的和，不過不知道怎麼用        
#%%
import collections
#matrix = [[0,1,0],[1,1,1],[0,1,0],[0,1,0]]
matrix = [[0,1,0],[1,1,1],[0,1,0]]
target=0

matrix = [[1,-1],[-1,1]]
target = 0


m, n = len(matrix), len(matrix[0])
#print('m',m)
row_sum = [[0]*(n+1) for i in range(m)]
print(row_sum)
# compute row presum
for i in range(m):
    row_sum[i][1]=matrix[i][0]
    for j in range(2,n+1):
#        print(i,j)
        row_sum[i][j]=matrix[i][j-1]+row_sum[i][j-1]
print(row_sum)

ans=0
# select each 2 columns and turns to problem 560
for i in range(n):
    for j in range(i+1,n+1):
        print(i,j)
        sub_matrix_sum = collections.defaultdict(int)
        sub_matrix_sum[0]=1
        cur_sum=0
        for k in range(m):
            cur_sum+=(row_sum[k][j]-row_sum[k][i])
            print(cur_sum)
            ans+= sub_matrix_sum[cur_sum-target]
            sub_matrix_sum[cur_sum]+=1
            print('ans',ans)
        print(sub_matrix_sum)
        print(ans)
print(ans)