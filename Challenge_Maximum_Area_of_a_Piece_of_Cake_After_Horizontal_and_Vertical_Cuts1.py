# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 18:03:59 2021

@author: ppj
"""

h = 5
w = 4

horizontalCuts = [1,2,4]
verticalCuts = [1,3]
horizontalCuts = [3,1]
verticalCuts = [1]
h = 5
w = 4
horizontalCuts = [3]
verticalCuts = [3]


horizontalCuts = sorted(horizontalCuts)
verticalCuts = sorted(verticalCuts)

max_h=horizontalCuts[0]
for i in range(1,len(horizontalCuts)):
    max_h=max(max_h,horizontalCuts[i]-horizontalCuts[i-1])
max_h=max(max_h,h-horizontalCuts[-1])

max_w=verticalCuts[0]
for i in range(1,len(verticalCuts)):
    max_w=max(max_w,verticalCuts[i]-verticalCuts[i-1])
max_w=max(max_w,w-verticalCuts[-1])

mod=10**9+7

print(((max_h%mod)*(max_w%mod))%mod)

