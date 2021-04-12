# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 00:13:53 2021

@author: ppj
"""

nums = [2,7,11,15]
target = 9
last_dic={}
for i in range(len(nums)):
#    print(last_dic)
#    print(nums[i])
    if nums[i] in last_dic:
#        print('here')
        print(i,last_dic[nums[i]])
    else:
        last_dic[target-nums[i]]=i