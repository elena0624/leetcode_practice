# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 00:03:13 2021

@author: ppj
"""

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [1]
nums = [5,4,-1,7,8]
nums = [-2,1]

#O(n)作法
lc_sum=-10**6
left=0
for i in range(len(nums)):
    # 比較在前n者的情況下是否要包含
    if left>0:
        #要包含左邊 那看看左邊有無比較大
        if nums[i]<0:
            lc_sum = left if left>lc_sum else lc_sum
        else:
            lc_sum = left+ nums[i] if (left+ nums[i])>lc_sum else lc_sum
        # 要包含左邊 更新左邊數字
        left = left + nums[i] 
        
    else:
        left = nums[i]
        # 步包含左邊 納比自己有沒有比目前最大值大
        lc_sum = nums[i] if nums[i]>lc_sum else lc_sum

print(lc_sum)
#%%
#nums = [-2,1,-3,4,-1,2,1,-5,4]
#nums = [1]
#nums = [5,4,-1,7,8]
nums = [-2,1]

#O(n)作法
lc_sum=-10**6
left=0

for i in range(len(nums)):
    left+=nums[i]
    lc_sum = max(left,lc_sum)
    left = max(left,0)
print(lc_sum)
#%% Recursion (Divide&conquer作法)

