# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 16:41:48 2021

@author: ppj
"""
# Wrong. Children with a higher rating get more candies than "their neighbors".

import collections


ratings = [1,2,2]
ratings_cnt = collections.Counter(ratings)

ans=0
can=1
for i in sorted(ratings_cnt.keys()):
    ans+=can*ratings_cnt[i]
    can+=1
print(ans)
#%%
#ratings = [1,2,2]
#ratings = [1,0,2]
#
#def con_large(i):
#    temp_ans=1
#    while i<len(ratings)-1 and ratings[i]>ratings[i-1]:
#        print('big',ratings[i])
#        cur+=1
#        temp_ans+=cur
#        i+=1
#    return i, temp_ans # 回傳的i為斷的第一個(下一個的頭)
#def con_small(i):
#    temp_ans=1
#    while i<len(ratings)-1 and ratings[i]<ratings[i-1]:
#        print('small',ratings[i])
#        cur+=1
#        temp_ans+=cur
#        i+=1
#    return i, temp_ans # 回傳的i為斷的第一個(下一個的頭)
#ans=0
#i=1
#while i<len(ratings):
#    if ratings[i]>ratings[i-1]:# 開啟連續大情況
#        
#        
#    print(ratings[i])
#    cur=1
#    ans+=cur
#    # 找連續大
#    while i<len(ratings)-1 and ratings[i+1]>ratings[i]:
#        print('big',ratings[i])
#        cur+=1
#        ans+=cur
#        i+=1
#        temp=cur
#    # 最後一個扣掉 歸到下一組
#    # 找連續小
#    while i<len(ratings)-1 and ratings[i+1]<ratings[i]:
#        print('small',ratings[i])
#        cur+=1
#        ans+=cur
#        i+=1
#        temp=1
#    
#    i+=1
##        temp=1
#    # 然後就可以繼續假裝從頭計算了
#print(ans)
#%%
ratings = [1,2,2]
ratings = [1,0,2]
ratings=[1,3,4,5,2]
ratings=[1,2,3,4,5,2,1]
candies = [1 for i in range(len(ratings))]
ans=0
for i in range(1,len(ratings)):
    if ratings[i]>ratings[i-1]:
        candies[i]=candies[i-1]+1
print(candies)
ans=candies[-1]
for i in range(len(ratings)-1,0,-1):
    if ratings[i-1]>ratings[i] and candies[i-1]<=candies[i]:
        candies[i-1]=candies[i]+1
    ans+=candies[i-1]
print(ans)
    