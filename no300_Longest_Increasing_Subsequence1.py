# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 19:36:20 2021

@author: ppj
"""

# 300 Longest Increasing Subsequence
nums = [10,9,2,5,3,7,101,18]

lis = [1]*len(nums)
for i in range(1,len(nums)):
    max_len=0
    for j in range(0,i):
        if nums[i]>nums[j]:
#            print('here')
            if lis[j]>max_len:
#                print('nums[j]',nums[j])
                max_len=lis[j]
    lis[i] = max_len+1
print(max(lis))

#%% nlong版本
nums = [10,9,2,5,3,7,101,18]

lis_bound = [nums[0]]

for i in range(1,len(nums)):
    if nums[i]>lis_bound[-1]:
        lis_bound.append(nums[i])
    elif nums[i]<lis_bound[0]:
        lis_bound[0]=nums[i]
    elif nums[i] in lis_bound:
        continue
    else:
        # 從lis_bound去找他所處的位置
        l=0
        r=len(lis_bound)-1
        while l<r:
            m=(l+r)//2
            if nums[i]>lis_bound[m]:# >m，因為找找比x大的，m也不用考慮了
                l=m+1
            else:#<m 因為要找比x大的,所以m也要考慮
                r=m
        lis_bound[r]=nums[i]
print(lis_bound)
print(len(lis_bound))
        