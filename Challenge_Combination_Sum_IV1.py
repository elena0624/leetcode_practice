# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 15:25:38 2021

@author: ppj
"""

nums = [1,2,3]
target = 4

nums = [9]
target = 3

nums = [4,2,1]
target = 32


cnt=0
def dfs_search(cur):
    global cnt
    if cur==target:
        cnt+=1
        print('cnt++',cnt)
        return
    elif cur>target:
        return
    else:
        for i in nums:
            print('i',i)
            print('cur',cur)
            dfs_search(cur+i)
    return

dfs_search(0)
print(cnt)

#%%
import collections
nums = [4,2,1]
target = 32

# 最基本
dp=collections.defaultdict(int)
for i in nums:
    dp[i]+=1
#print(dp)

for i in range(target+1):
    temp=0
    temp+=dp[i]
    for j in nums:
#        print('i-j',i-j,'dp[i-j]',dp[i-j])
        temp+=dp[i-j]
    dp[i]=temp
print(temp)
#%%
import collections
nums = [4,2,1]
target = 32

dp=collections.defaultdict(int)
dp[0]=1

for i in range(target+1):
    temp=0
    temp+=dp[i]
    for j in nums:
        temp+=dp[i-j]
    dp[i]=temp
print(temp)


