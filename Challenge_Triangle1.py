# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 15:15:35 2021

@author: ppj
"""
# 這是錯的
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-1],[2,3],[1,-1,-3]]
ans=0
for i in triangle:
    ans+=min(i)
print(ans)
    
#%%
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-1],[2,3],[1,-1,-3]]

if len(triangle)==1:
    print(triangle[0][0])
for i in range(len(triangle)-2,-1,-1):
    print('tra i',triangle[i])
    cur_stack=[]
    if i==len(triangle)-2:
        last_stack=triangle[-1]
    print(cur_stack)
    print(last_stack)

    for j in range(len(triangle[i])):
        cur_stack.append(triangle[i][j]+min(last_stack[j],last_stack[j+1]))
    print('c',cur_stack)
    print('l',last_stack)

    last_stack=cur_stack
print(cur_stack[0])
#%% Try to revised
triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-1],[2,3],[1,-1,-3]]

last_stack=triangle[-1]
for i in range(len(triangle)-2,-1,-1):
    for j in range(len(triangle[i])):
        last_stack[j]=triangle[i][j]+min(last_stack[j],last_stack[j+1])
    print(last_stack)
print(last_stack[0])
