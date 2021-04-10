# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 16:52:03 2021

@author: ppj
"""
from functools import lru_cache
#matrix = [[9,9,4],[6,6,8],[2,1,1]]
matrix = [[3,4,5],[3,2,6],[2,2,1]]
matrix = [[1]]

#紀錄最長路徑的table
m=len(matrix)
n=len(matrix[0])
rec=[[0]*n for i in range(m)]
print(rec)
seen=set()
queue=[]

temp=[[1]*n for i in range(m)]
@lru_cache(None)
def dfs(depth,i,j):
    print('depth',depth)
    print('temp',temp)
    if not searchNeighbor(i,j):
        print('ij',i,j)
        temp[i][j]=max(temp[i][j],depth)
#        if depth>max_depth:
#            max_depth=depth
        return
    for a,b in searchNeighbor(i,j):
        print(a,b)
        if depth<temp[i][j]:##如果比較少的應該不用走了?
            return
        dfs(depth+1,a,b)
        temp[i][j]=max(temp[i][j],depth)

# 從每一個點作為起點開始走
@lru_cache(None)
def searchNeighbor(i,j):
    available=[]
    # 上
    if i-1>=0:
        if matrix[i-1][j]>matrix[i][j]:
            available.append((i-1,j))
    # 下
    if (i+1)<=(m-1):
        if matrix[i+1][j]>matrix[i][j]:
            available.append((i+1,j))
    # 左
    if (j-1)>=0:
        if matrix[i][j-1]>matrix[i][j]:
            available.append((i,j-1))
    # 右
    if (j+1)<=(n-1):
        if matrix[i][j+1]>matrix[i][j]:
            available.append((i,j+1))
    return available

# 從每一個點作為起點開始走
def checkNeighbor(i,j):
    available=[]
    # 上
    if i-1>=0:
        if matrix[i-1][j]<matrix[i][j]:
            available.append((i-1,j))
    # 下
    if (i+1)<=(m-1):
        if matrix[i+1][j]<matrix[i][j]:
            available.append((i+1,j))
    # 左
    if (j-1)>=0:
        if matrix[i][j-1]<matrix[i][j]:
            available.append((i,j-1))
    # 右
    if (j+1)<=(n-1):
        if matrix[i][j+1]<matrix[i][j]:
            available.append((i,j+1))
    return available

temp=[[1]*n for i in range(m)]
max_depth=0
for i in range(m):
    for j in range(n):
        if not checkNeighbor(i,j):# 代表周圍沒有更小
            print('aaa',i,j)
            dfs(1,i,j)
print((max(max(x) for x in temp)))
#%%
matrix = [[9,9,4],[6,6,8],[2,1,1]]
#matrix = [[3,4,5],[3,2,6],[2,2,1]]
#matrix = [[1]]

m=len(matrix)
n=len(matrix[0])
@lru_cache(None)
def dfs(i,j):
    if not searchNeighbor(i,j):
        temp[i][j]=1
        return 1
    if temp[i][j]>0:
        return temp[i][j]
    else:
        temp[i][j]=max(dfs(a,b)+1 for a,b in searchNeighbor(i,j))
#    print(temp)
    return temp[i][j]
@lru_cache(None)
def searchNeighbor(i,j):
    available=[]
    # 上
    if i-1>=0:
        if matrix[i-1][j]>matrix[i][j]:
            available.append((i-1,j))
    # 下
    if (i+1)<=(m-1):
        if matrix[i+1][j]>matrix[i][j]:
            available.append((i+1,j))
    # 左
    if (j-1)>=0:
        if matrix[i][j-1]>matrix[i][j]:
            available.append((i,j-1))
    # 右
    if (j+1)<=(n-1):
        if matrix[i][j+1]>matrix[i][j]:
            available.append((i,j+1))
    return available

temp=[[0]*n for i in range(m)]
max_depth=0
for i in range(m):
    for j in range(n):
        dfs(i,j)
print((max(max(x) for x in temp)))

#%% Try to accelerate
matrix = [[9,9,4],[6,6,8],[2,1,1]]
#matrix = [[3,4,5],[3,2,6],[2,2,1]]
#matrix = [[1]]

m=len(matrix)
n=len(matrix[0])
@lru_cache(None)
def dfs(i,j):
    if temp[i][j]>0:
        return temp[i][j]

    available=[]
    # 上
    if i-1>=0:
        if matrix[i-1][j]>matrix[i][j]:
            available.append((i-1,j))
    # 下
    if (i+1)<=(m-1):
        if matrix[i+1][j]>matrix[i][j]:
            available.append((i+1,j))
    # 左
    if (j-1)>=0:
        if matrix[i][j-1]>matrix[i][j]:
            available.append((i,j-1))
    # 右
    if (j+1)<=(n-1):
        if matrix[i][j+1]>matrix[i][j]:
            available.append((i,j+1))
    if not available:
        return 1
    temp[i][j]=max(dfs(a,b)+1 for a,b in available)
#    print(temp)
    return temp[i][j]

temp=[[0]*n for i in range(m)]
max_depth=0
for i in range(m):
    for j in range(n):
        max_depth=max(max_depth,dfs(i,j))
print(max_depth)