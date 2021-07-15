# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 21:51:56 2021

@author: ppj
"""
import bisect
nums = [4,2,3,4]


ans=0
nums = sorted(nums)

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        idx = bisect.bisect_left(nums,nums[i]+nums[j])
#        print('i',i,'j',j,'idx',idx)
#        print(max(0,idx-1-j))
        ans+=max(0,idx-1-j)
print(ans)
    