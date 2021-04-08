# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 22:49:52 2021

@author: ppj
"""

#nums = [100,4,200,1,3,2]
nums = [0,3,7,2,5,8,4,6,0,1]

nums = sorted(list(set(nums)))
i=0
lg_ans=0
while i<len(nums):
    ans=1
    r=i
    while r<(len(nums)-1) and ((nums[r]+1)==nums[r+1]):
#        print((nums[r]+1))
#        print(nums[r+1])

        r+=1
        ans+=1
    lg_ans = max(lg_ans, ans)
    i=r+1
print(lg_ans)   