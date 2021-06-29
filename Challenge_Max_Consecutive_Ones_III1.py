# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:14:10 2021

@author: ppj
"""

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
nums = [0,0,0,1]
k = 4
for i in range(len(nums),0,-1):
    z_cnt=i-sum(nums[:i])
    print('zcnt',z_cnt)
    if z_cnt<=k:
        print(i)
        break
    for j in range(1,len(nums)-i+1):
        z_cnt-=(nums[j-1]==0)# 頭要不要扣
#        print('head',nums[j-1])
#        print('head zcnt',z_cnt)
        z_cnt+=(nums[j+i-1]==0)# 尾要不要扣
#        print('tail',nums[j+i-1])
#        print('tail zcnt',z_cnt)
        
        if z_cnt<=k:
            print(i)
            break
#%% 換個
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3   
nums = [0,0,0]
k = 0
i=0
l=0
while (i+l)<len(nums):# 從起點開始
    print('i',i)
    print('l',l)
    z_cnt=l-sum(nums[i:i+l])
    print('z_cnt',z_cnt)
    while z_cnt<=k and (i+l)<len(nums):# 看最長到多長
        z_cnt+=(nums[i+l+1]==0)
        l+=1
    l-=1
    i+=1
print(l)
        
#%% 
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

nums = [0,0,0]
k = 0

z_cnt=0
left=0 # 起點
ans=0
for i in range(len(nums)):# 檢查每一個是不是0
    if nums[i]==0:
        z_cnt+=1
#    print(z_cnt)
    while z_cnt>k: #若目前要改的已經超過 要把起始點移到不會超過的地方(最慘就是直接移到i的右邊)
        if nums[left]==0:
            z_cnt-=1
        left+=1
    ans=max(ans,i-left+1)   
print(ans)
        
#%%
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

#nums = [0,0,0]
#k = 0


i = 0
for j in range(len(nums)):
    k -= 1 - nums[j]
    if k < 0:
        k += 1 - nums[i]
        i += 1
print(j - i + 1)
