# -*- coding: utf-8 -*-
"""
Created on Mon May  3 15:32:32 2021

@author: ppj
"""

nums = [3,1,2,10,1]

for i in range(1,len(nums)):
    nums[i]+=nums[i-1]
print(nums)