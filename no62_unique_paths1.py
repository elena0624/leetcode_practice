# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 23:22:36 2021

@author: ppj
"""
#%%
# 初始的步數紀錄
n=3
m=3
maze = [[0],[1]*(n+1)] # 列存往下走m,行存往右走n
# m=0的時候都不會有解=>0;m=1,n=0=>0;m=1,n=1=>1(原地),m=1,n=2=>1
# m=2,n=0=>0;m=2,n=1=>1;m=2,n=2=>2
for i in range(2,m+1):
    maze.append([0,1])
    for j in range(2,n+1):
        maze[i].append(maze[i-1][j] + maze[i][j-1])
print(maze)
print(maze[m][n])


#%%
# 想節省空間=>一次只保留最後一列
m=3
n=3

if m==1 or n==1:
    print(1)
else:
# 最新一列
    n_row = [1]*(n-1) # 第一列都是1 (index=0~n-2)
    for i in range(0,m-1):
        # 目前的那個
        target = 1 # 第一個都是1
        for j in range(0,n-1):
            target = n_row[j] + target
            n_row[j] = target
    print(n_row)
    print(target)
#%%
# 優化=>有沒有發現target跟n_row[j]是重複的!! 沒錯 其實就是保留前一個=剛剛算完的那一個
# 可以再省掉target的空間
m=3
n=3
# 最新一列
n_row = [1]*n # 第一列都是1 (index=0~n-1)
for _ in range(1,m): # 有幾列其實不會用到,只是要執行那麼多次而已
    for j in range(1,n):
        n_row[j] = n_row[j] + n_row[j-1] # n_row[0]永遠是1不會被更新到
print(n_row)
print(n_row[-1])


#%%
# 討論區答案
m=3
n=3
path_count = [1] * m
for _ in range(1, n):
    for i in range(1, m):
        path_count[i] += path_count[i-1]
print( path_count)
    