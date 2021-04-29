# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 23:26:48 2021

@author: ppj
"""

nums = [5,7,7,8,8,10]
target = 8

nums = [5,7,7,8,8,10]
target = 6

nums = []
target = 0

nums = [2,2]
target = 2

nums = [1,4]
target = 4
#nums = [1]
#target = 1

n=len(nums)
l=0
r=n-1
mid = (l+r)//2
f_ans=-1
if not nums:
    print([-1,-1])

while mid!=l and mid!=r:
    print(l,r,mid)
    if target<nums[mid]:
        r=mid
    elif target==nums[mid]:
        f_ans=mid
        break
    else:
        l=mid
    mid=(l+r)//2
if target==nums[mid]:
    f_ans=mid
elif target==nums[r]:
    f_ans=r
elif target==nums[l]:
    f_ans=l
    
if f_ans==-1:
    print([-1,-1])
else:
    # 從前後找
    s_ans=f_ans
    l_ans=f_ans
    while (s_ans>0 and nums[s_ans-1]==target) or (l_ans<n-1 and nums[l_ans+1]==target):
        if s_ans>0 and nums[s_ans-1]==target:
            s_ans-=1
        if l_ans<n-1 and nums[l_ans+1]==target:
            l_ans+=1
print([s_ans,l_ans])
    

    
        
    