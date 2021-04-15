# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 15:52:54 2021

@author: ppj
"""

n=1

dp_1=0
dp=1
cur=0
if n==0:
    print(dp_1)

for i in range(n-1):
    cur=dp_1+dp
    dp_1=dp
    dp=cur
print(dp)
    
