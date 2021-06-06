# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 19:51:57 2021

@author: ppj
"""
#%% TLE answer
n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2

n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 3

n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 4

mod=10**9+7
speed = [x for _,x in sorted(zip(efficiency,speed))]
efficiency = sorted(efficiency)

max_ans=0
for i in range(n):
    cur_eff = efficiency[i]
    cur_speed = speed[i] + sum(sorted(speed[i+1:],reverse=True)[:min(k-1,len(speed[i+1:]))])    
    print(cur_eff,cur_speed)
    max_ans=max(max_ans,cur_eff*cur_speed)
print(max_ans%mod)
#%% 還是TLE
# 改這樣應該要n^2
n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2

n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 3

n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 4

mod=10**9+7
#speed = [x for _,x in sorted(zip(efficiency,speed))]
#efficiency = sorted(efficiency)

#speed2 = sorted(enumerate(speed),key=lambda x:x[1],reverse=True)
speed2 = sorted(zip(speed,efficiency),reverse=True)
efficiency = sorted(efficiency)

max_ans=0
for i in range(n):
    cur_eff = efficiency[i]
    temp_idx=0
    j=0
    cur_speed=0
    while j<n and temp_idx<k:
        if speed2[j][1]>=cur_eff:
            cur_speed+=speed2[j][0]
            temp_idx+=1
        j+=1
#    print(cur_eff,cur_speed)
    max_ans=max(max_ans,cur_eff*cur_speed)
print(max_ans%mod)
#%%
# 要用priority queue概念
import heapq

n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2

n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 3

n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 4

mod=10**9+7
speed = [x for _,x in sorted(zip(efficiency,speed), reverse=True)]
efficiency = sorted(efficiency, reverse=True)

heap_speed = []
sum_speed = 0
max_ans=0
for i in range(n):
#    print(heap_speed)
    if len(heap_speed)<k:
        heapq.heappush(heap_speed,speed[i])
        sum_speed+=speed[i]
    else:
        sum_speed+=speed[i]
        sum_speed-= heapq.heappushpop(heap_speed, speed[i])
    max_ans=max(max_ans,efficiency[i]*sum_speed)
print(max_ans%mod)
