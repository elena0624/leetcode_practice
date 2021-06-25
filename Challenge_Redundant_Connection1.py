# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 20:40:07 2021

@author: ppj
"""
import collections

edges = [[1,2],[1,3],[2,3]]
edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]

new_edges=collections.defaultdict(set)# 用來記錄每個點可以到哪裡

def bfs(a):
    seen=set()
    stack=list(new_edges[a])
    while stack:
        cur=stack.pop()
#        if cur==b:
#            return True
        if cur in seen:
            continue
        seen.add(cur)
        stack.extend(new_edges[cur])
        new_edges[a].add(cur)
        new_edges[cur].add(a)
        
        
        
    

for a,b in edges:   
    # 檢查是否已經可傳入
    bfs(a)
    if a in new_edges[b] or b in new_edges[a]:
        print([a,b])
    # 沒有的話更新
    new_edges[a].add(b)
    new_edges[b].add(a)
    
    
    
    