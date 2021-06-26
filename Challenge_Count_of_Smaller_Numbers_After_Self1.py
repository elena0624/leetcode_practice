# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 16:34:56 2021

@author: ppj
"""

nums = [5,2,6,1]

ans=[]
for i in range(len(nums)):
    cur=0
    for j in range(i+1,len(nums)):
        if nums[j]<nums[i]:
            cur+=1
    ans.append(cur)
print(ans)
#%%
nums = [5,2,6,1]

import bisect
ans=nums.copy()
sorted_cnt=[]
for i in range(len(nums)-1,-1,-1):
    pos=bisect.bisect_left(sorted_cnt,nums[i])
    ans[i]=pos
    sorted_cnt.insert(pos,nums[i])
print(ans)
#%%

nums = [5,2,6,1]

rank, N, res = {val: i + 1 for i, val in enumerate(sorted(nums))}, len(nums), []
BITree = [0] * (N + 1)

def update(i):
    while i <= N:
        BITree[i] += 1
        i += (i & -i)
    
def getSum(i):
    s = 0
    while i:
        print(i)
        s += BITree[i]
        i -= (i & -i)
        print('2',i)
    return s

for x in reversed(nums):
    res += getSum(rank[x] - 1),
    update(rank[x])
    print(BITree)