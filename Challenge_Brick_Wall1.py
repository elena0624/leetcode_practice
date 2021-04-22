# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 20:30:01 2021

@author: ppj
"""
wall=[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
#wall=[[1],[1],[1]]
#wall=[[100000000],[100000000],[100000000]]

through=[len(wall)]*(sum(wall[0]))
for i in range(len(wall)):
    print('i',i)
    cur_brick=0
    for j in wall[i]:
        print('j',j)
        cur_brick+=j
        print('curbruick',cur_brick)
        through[cur_brick-1]-=1
ans=min(through[:-1]) if through[:-1] else len(wall)
print(ans)
        
#%%
import collections
#wall=[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
wall=[[1],[1],[1]]
#wall=[[100000000],[100000000],[100000000]]
#wall=[[1,1],[2],[1,1]]
through=collections.defaultdict(int)
#through=dict.setdefault(key, default=len(wall))
#through=[len(wall)]*(sum(wall[0]))
#through={}
for i in range(len(wall)):
    print('i',i)
    cur_brick=0
    for j in wall[i]:
        print('j',j)
        cur_brick+=j
        print('curbruick',cur_brick)
        if cur_brick!=sum(wall[0]):
            through[cur_brick-1]-=1
if through:
    print(min(list(through.values()))+len(wall))
else:
    print(len(wall))
#ans=min(through[:-1]) if through[:-1] else len(wall)
#print(ans)
    
#%% Revised
import collections
wall=[[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
#wall=[[1],[1],[1]]
#wall=[[100000000],[100000000],[100000000]]
#wall=[[1,1],[2],[1,1]]
through=collections.defaultdict(int)
#through=dict.setdefault(key, default=len(wall))
#through=[len(wall)]*(sum(wall[0]))
#through={}
for i in range(len(wall)):
    print('i',i)
    cur_brick=0
    for j in wall[i][:-1]:
        print('j',j)
        cur_brick+=j
        print('curbruick',cur_brick)
        through[cur_brick-1]-=1
if through:
    print(min(list(through.values()))+len(wall))
else:
    print(len(wall))
