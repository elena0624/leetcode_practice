# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 19:26:35 2021

@author: ppj
"""
import collections
nums = [1,1,1]
k = 2

#nums = [1,2,3]
#k = 3

#nums=[1]
#k=1

sum_nums = nums.copy()
m=len(nums)
sum_dict = collections.defaultdict(list)
sum_dict[sum_nums[0]].append(0)
for i in range(1,m):
    sum_nums[i]+=sum_nums[i-1]
    sum_dict[sum_nums[i]].append(i)

ans=0
ans+=len(sum_dict[k])
print(ans)
for i in range(m):
#        print('i',i)
#        print(ans)
#        print([a>=i for a in sum_dict[sum_nums[i]+k]])
#        print(i)
#        print([a for a in sum_dict[sum_nums[i]+k]])
    print(sum_nums[i])
    ans+=sum(a>i for a in sum_dict[sum_nums[i]+k])
    print(sum_dict[sum_nums[i]+k])
    print([a for a in sum_dict[sum_nums[i]+k]])
    print(sum(a>i for a in sum_dict[sum_nums[i]+k]))
    print(ans)
#        print(sum_dict[sum_nums[i]+k])
#        print('1234',sum(a>=i for a in sum_dict[sum_nums[i]+k]))
        
print(ans)
#print(temp_dict)
#%%
nums = [1,2,3]
k = 3

m=len(nums)
sum_cnt = collections.defaultdict(int)
sum_cnt[0]=1
ans=0
cur_sum=0
for i in range(m):
#    print('i',i)
#    print(sum_cnt)
#    print(nums[i])
#    print('ans',ans)
    cur_sum+=nums[i]
    ans+=sum_cnt[cur_sum-k]
    sum_cnt[cur_sum]+=1
print(ans)
    
    
