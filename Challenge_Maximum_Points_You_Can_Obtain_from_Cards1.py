# -*- coding: utf-8 -*-
"""
Created on Tue May 11 22:47:22 2021

@author: ppj
"""

cardPoints = [1,2,3,4,5,6,1]
k = 3

#cardPoints = [2,2,2]
#k = 2

cardPoints = [9,7,7,9,7,7,9]
k = 7

cardPoints = [1,1000,1]
k = 1

cardPoints = [1,79,80,1,1,1,200,1]
k = 3

n=len(cardPoints)
sum_n = sum(cardPoints)
sum_other = sum(cardPoints[:(n-k)])
min_other = sum_other

for i in range(n-k,n):
    print(i)
    sum_other = sum_other+cardPoints[i]-cardPoints[i-n+k]
    min_other = min(min_other,sum_other)
    
print(sum_n-min_other)
    