# -*- coding: utf-8 -*-
"""
Created on Tue May  4 17:13:54 2021

@author: ppj
"""

nums = [4,2,3]
nums = [4,2,1]
nums = [-1,4,2,3]
nums=[5,7,1,8]
nums = [3,4,2,3]

violate = False
#i=1
#while i<len(nums):
for i in range(1,len(nums)):
    print('i',i)
    print(nums[i-1],nums[i])
#    print(violate)
    print(nums)
    if nums[i]<nums[i-1]:
        if violate:
            print('??')
            print(False)
            break
        else:
            print('???')
            # 如果發生在最後一個就沒差
            if i==len(nums)-1:
                print(True)
#            elif i==1:
#                continue
            elif i>1 and nums[i+1]<nums[i-1] and nums[i]<nums[i-2]:
#                nums[i-1]=nums[i]
                # 要回去檢查
#                if i>1 and nums[i-1]<nums[i-2]:
                    print(False)
                    break
#            else:@ 如果改當下的就沒差
#                nums[i]=nums[i-1]
                
                
#            print(nums[i+1], nums[i-1])
#            if i<len(nums)-1 and nums[i+1]<nums[i-1]:
#                print(False)
#                break
            violate=True
        # i不變 再看看還行不行
    
#    else:#符合就繼續檢查
#        i+=1
#    i+=1
#if violate and nums[1]<nums[0]:
#    print(False)
print(True)
        
    