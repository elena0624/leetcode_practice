# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:11:46 2021

@author: ppj
"""

nums=[1,2,3,1]
nums=[1]
l=0
r=len(nums)-1
while l<r:
    print(l,r)
    mid = (l+r)//2
    if nums[mid]>nums[mid+1]:
        r=mid
    else:
        l=mid+1
print(l)
