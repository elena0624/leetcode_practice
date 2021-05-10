# -*- coding: utf-8 -*-
"""
Created on Mon May 10 12:20:03 2021

@author: ppj
"""
import heapq
target = [9,3,5]
#target = [1,1,1,2]
#target = [8,5]
#target = [9,9,9]
#target = [1,1000000000]
target = [2,900000001]
n=len(target)
cnt_1 = target.count(1)
if cnt_1>0:
    target.remove(1)
for a in target:
    if a<n:
        print(False)

target = [-1*a for a in target]

heapq.heapify(target)
#while target[0]<-1:
while cnt_1<n and len(target)>1:
    print(target)
    cur_large = heapq.heappop(target)
    prev_large = cur_large-sum(target)+cnt_1
    print(prev_large)
    if prev_large==-1:
        cnt_1+=1
    elif prev_large>-1*n:
        print('here')
        print(False)
        break
    else:
        heapq.heappush(target,prev_large)

if cnt_1==n:
    print(True)
if len(target)==1 and (target[0]+1)%(cnt_1)==0:
    print(True)
else:
    print(False)
#if target[0]==-1 and max(target)==-1:
#    print(True)
#else:
#    print(False)
#%%
import heapq
target = [9,3,5]
target = [1,1,1,2]
target = [8,5]
#target = [9,9,9]
#target = [1,1000000000]
#target = [2,900000001]
target=[2]
n=len(target)
if n==1:
    a=True if target[0]==1 else False
    print(a)
target = [-1*a for a in target]
heapq.heapify(target)

while target[0]<-1:
    print('TARGET',target)
    cur_large = heapq.heappop(target)
#    print('//////8',cur_large)
    print(target)
    other_sum = sum(target)
    sec_large = target[0]
    if sec_large==-1:
      if (cur_large+1)%other_sum==0:
          print(True)
          break
      else:
          print('here1')
          print(False)
          break
    prev_large = cur_large-(((cur_large-sec_large)//other_sum)+1) * other_sum
#    if prev_large==-1:
#        cnt_1+=1
    if prev_large>-1:
        print('here2')
        print(False)
        break
    heapq.heappush(target,prev_large)
if target.count(-1)==n:
    print(True)
else:
    print(False)
#print(False)
#if cnt_1==n:
#    print(True)
#else:
#    print(False) 
#%%
import heapq
target = [9,3,5]
#target = [1,1,1,2]
#target = [8,5]
#target = [9,9,9]
#target = [1,1000000000]
#target = [2,900000001]
#target=[2]
n=len(target)
if n==1:
    a=True if target[0]==1 else False
    print(a)
target = [-1*a for a in target]
heapq.heapify(target)
other_sum=sum(target)
while target[0]<-1:
    print('TARGET',target)
    cur_large = heapq.heappop(target)
#    print('//////8',cur_large)
    print(target)
#    other_sum = sum(target)
    other_sum-=cur_large
    sec_large = target[0]
    if sec_large==-1:
      if (cur_large+1)%other_sum==0:
          print(True)
          break
      else:
          print('here1')
          print(False)
          break
    prev_large = cur_large-(((cur_large-sec_large)//other_sum)+1) * other_sum
#    if prev_large==-1:
#        cnt_1+=1
    if prev_large>-1:
        print('here2')
        print(False)
        break
    heapq.heappush(target,prev_large)
    other_sum+=prev_large
#if target.count(-1)==n:
#    print(True)
#else:
#    print(False)
#%%
