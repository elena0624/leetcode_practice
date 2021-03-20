# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 03:46:15 2021

@author: ppj
"""
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
maze = obstacleGrid.copy()
#先初始化第一列
#maze[0][0]=1 # 結果有左上角就擺石頭的
# 先判斷如果左上是石頭或終點是石頭就不用玩了
if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
    print(0) # return
maze[0][0]=1 
for i in range(len(maze[0])-1):
    if obstacleGrid[0][i+1]==0 and maze[0][i]==1:
        maze[0][i+1]=1
    else:
        maze[0][i+1]=0
#初始化第一行
for i in range(len(maze)-1):
    if obstacleGrid[i+1][0]==0 and maze[i][0]==1:
        maze[i+1][0]=1
    else:
        maze[i+1][0]=0

for i in range(1,len(maze)):
    for j in range(1,len(maze[0])):
        if obstacleGrid[i][j]==1:
            maze[i][j]=0
        else:
            maze[i][j]=maze[i-1][j]+maze[i][j-1]

#obstacleGrid[0]=[1]*len(obstacleGrid[0])
print(maze)
print(maze[-1][-1])
#obstacleGrid[:][0]=1

#%%
# 改成存在同一個
obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
#maze = obstacleGrid.copy()
#先初始化第一列
#maze[0][0]=1 # 結果有左上角就擺石頭的
# 先判斷如果左上是石頭或終點是石頭就不用玩了
if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
    print(0) # return

obstacleGrid[0][0] = 1 # 左上不是1(障礙),那就是1(1條路)
for i in range(len(obstacleGrid[0])-1):
    if obstacleGrid[0][i+1]==0 and obstacleGrid[0][i]==1:
        obstacleGrid[0][i+1]=1
    else:
        obstacleGrid[0][i+1]=0
print(obstacleGrid)
#初始化第一行
for i in range(len(obstacleGrid)-1):
    if obstacleGrid[i+1][0]==0 and obstacleGrid[i][0]==1:
        obstacleGrid[i+1][0]=1
    else:
        obstacleGrid[i+1][0]=0

for i in range(1,len(obstacleGrid)):
    for j in range(1,len(obstacleGrid[0])):
        if obstacleGrid[i][j]==1:
            obstacleGrid[i][j]=0
        else:
            obstacleGrid[i][j]=obstacleGrid[i-1][j]+obstacleGrid[i][j-1]

#obstacleGrid[0]=[1]*len(obstacleGrid[0])
print(obstacleGrid)
print(obstacleGrid[-1][-1])
#obstacleGrid[:][0]=1