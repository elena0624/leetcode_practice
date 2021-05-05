# -*- coding: utf-8 -*-
"""
Created on Wed May  5 15:28:02 2021

@author: ppj
"""

nums = [2,3,1,1,4]

stack=[]
n=len(nums)
steps=0
def bfs(goal,steps):
    if goal<=nums[0]:
        return steps+1
    depart=[]
    for i in range(1,goal):
        if (goal-i)<=nums[i]:
            depart.append(i)
            
            
    
bfs(n-1,steps)


#%%
nums = [2,3,1,1,4]
#nums = [0]
#nums = [1,2]
#unreach=set(range(1,n-1))

n=len(nums)
unreach=list(range(n-1))

steps=0
pre_steps=[n-1]
while unreach:
    steps+=1
    print(unreach)
    print(pre_steps)
    cur_steps=[]
    for j in pre_steps:
        if j<=nums[0]:
            print(steps)
            unreach=[]
            break
        for i in unreach:
            if (j-i)<=nums[i]:
                unreach.remove(i)
                cur_steps.append(i)
    pre_steps=cur_steps

print(steps)