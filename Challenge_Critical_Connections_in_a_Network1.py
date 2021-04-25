# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 12:23:51 2021

@author: ppj
"""

import collections

n = 4
connections = [[0,1],[1,2],[2,0],[1,3]]

adj=collections.defaultdict(set)
for v1,v2 in connections:
    adj[v1].add(v2)
    adj[v2].add(v1)

time=0
low=[-1]*n
#low=[-1]*n
#father=[-1]*n
ans=[]

def dfs(cur_node:int, father:int, time:int, low:list, ans:list, adj)->int:
    print('time..',time)
    time+=1###
#    low[cur_node]=time+1 # 初始的話就跟dfn是同步的
    low[cur_node]=time###
    for child in adj[cur_node]:
        if child==father: # 訪問過,如果是父節點就雙向不用再考慮一次
            continue
        elif low[child]==-1:# 還未訪問過
#            low[cur_node] = min(low[cur_node],dfs(child,cur_node,time+1,low,ans,adj))#返回孩子最小的節點 更新下限
            low[cur_node] = min(low[cur_node],dfs(child,cur_node,time,low,ans,adj))###
            
        else: #訪問過了且也不是父節點=> back edge??
            low[cur_node] = min(low[cur_node],low[child])
    ## 現在經過cur node以下dfs探索完之後要檢查是不是bridge
    # bridge條件=> low child比dfn自己大
#        if low[child]>time+1: # 如果比自己大
#            ans.append([cur_node,child])
    # 影片的做法=> 全部遍歷完再一起判斷就好 因為自己的low沒被更新代表也無法超前父親的node
    print('low',low)
    print('time',time)
#    if low[cur_node]==time+1 and father!=-1:# 因為沒有父節點 自然也不用加入這一條edge(這一條edge不存在)
    if low[cur_node]==time and father!=-1:###
        ans.append([father,cur_node])        
        
    return low[cur_node]
    

# 隨便取一點=>0
dfs(0,-1,time,low,ans,adj)

print(ans)
