# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 01:05:54 2021

@author: ppj
"""
# Brute Force=>TLE
A = [1,0,2]
A = [1,2,0]

for i in range(len(A)):
    for j in range(i+2,len(A)):
        print('i',i,A[i])
        print('j',j,A[j])
        if A[i]>A[j]:
            print(False)
            break
print(True)

#%%
#A = [1,0,2]
#A = [1,2,0]
A = [0,1,3,2,5,4,6,8,7,10,9,12,11,14,13,15,16,18,17,19,21,20]
#A=[2,0,1]
# 
lc_min=5000
for i in range(len(A)-1,1,-1):#
    if A[i]<lc_min:
        lc_min = A[i]

    if A[i-2]>lc_min:
        print(False)
print(True)
#%% alternative solution
A = [1,0,2]
A = [1,2,0]
A = [0,1,3,2,5,4,6,8,7,10,9,12,11,14,13,15,16,18,17,19,21,20]
A=[2,0,1]
    
for i in range(len(A)):
    if A[i]<(i-1) or A[i]>(i+1):
        print(False)
print(True)

