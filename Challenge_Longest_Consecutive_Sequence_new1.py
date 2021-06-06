# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 16:48:12 2021

@author: ppj
"""
#import collections

nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]
#occ = [0]*2*10**9+1
#for i in nums:
#    occ[i+10**9]=1

nums2 = nums.copy

def dfs(i,l):
    if i-1 in nums and i-1 not in seen:
        seen.add(i-1)
        l=dfs(i-1,l+1)
    if i+1 in nums and i+1 not in seen:
        seen.add(i+1)
        l=dfs(i+1,l+1)
    return l 

max_ans=0
seen=set()
for i in nums:
    if i not in seen:
        seen.add(i)
        max_ans = max(dfs(i,1),max_ans)
print(max_ans)
        
    
#%%

nums = [100,4,200,1,3,2]
#nums = [0,3,7,2,5,8,4,6,0,1]
#occ = [0]*2*10**9+1
#for i in nums:
#    occ[i+10**9]=1

#nums2 = set(nums)

max_ans=0
un_seen=set(nums)
for i in range(len(nums)):
    cur_l=0
    if nums[i] in un_seen:
#        seen.add(nums[i])
        un_seen.remove(nums[i])
        cur_l=1
        l=r=nums[i]
        while l-1 in un_seen:
#        while l-1 in nums2:
            l-=1
            un_seen.remove(l)
#            seen.add(l)
            cur_l+=1
        while r+1 in un_seen:
#        while r+1 in nums2:
            r+=1
            un_seen.remove(r)
#            seen.add(r)
            cur_l+=1
        max_ans = max(cur_l,max_ans)
print(max_ans)
