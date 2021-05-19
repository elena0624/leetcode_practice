# -*- coding: utf-8 -*-
"""
Created on Wed May 19 17:17:31 2021

@author: ppj
"""

nums = [1,10,2,9]
nums = [1,0,0,8,6]

mean = sum(nums)//len(nums)

print(sum(abs(num-mean) for num in nums))
#print(n)