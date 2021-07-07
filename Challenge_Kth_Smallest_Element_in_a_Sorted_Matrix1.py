# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 18:08:11 2021

@author: ppj
"""
import heapq

matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

matrix = [[-5]]
k = 1


m=len(matrix)
n=len(matrix[0])

# 從前面
#if k<=(m*n//2):
# 先都從最前面

# 紀錄每一列現在紀到哪裡
idx_ls = [0 for i in range(m)]
stack=[]
# 把每一列的第一個先加進去一個sorted的list
for i in range(m):
    heapq.heappush(stack,(matrix[i][idx_ls[i]],i))
while k>0:
    print(k,stack)
    ans=heapq.heappop(stack)
    print(ans)
    idx_ls[ans[1]]+=1
    print(idx_ls)
    # 丟一個補一個 除非已經沒得補
    if idx_ls[ans[1]]<n:
        heapq.heappush(stack,(matrix[ans[1]][idx_ls[ans[1]]],ans[1]))
    k-=1
print(ans[0])
    

# 從後面
#else:
