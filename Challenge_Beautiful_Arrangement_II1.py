# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 18:07:08 2021

@author: ppj
"""

n=5
k=2

ans=list(range(1,n+1))
idx=1
for i in range(k,0,-1):
    if idx%2==1:
        ans[idx] =ans[idx-1]+i
    else:
        ans[idx] =ans[idx-1]-i
    idx+=1
print(ans)
   