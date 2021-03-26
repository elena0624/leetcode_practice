# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 01:25:41 2021

@author: ppj
"""

# Word Subsets
#A = ["amazon","apple","facebook","google","leetcode"]
#B = ["e","o"]
A = ["amazon","apple","facebook","google","leetcode"]
B = ["lo","eo"]

import collections
ans_list = []
bb_counter = collections.Counter()
for b in B:
    bb_counter = bb_counter | collections.Counter(b) # 交集
for a in A:
    a_counter = collections.Counter(a)
    a_counter.subtract(bb_counter)
#    print(-a_counter)
    if not (-a_counter):
        print("universal",a)
        ans_list.append(a)
print(ans_list)
    
#    print(a_counter)
#    print(bb_counter)
    
#%%
A = ["amazon","apple","facebook","google","leetcode"]
B = ["lo","eo"]


ans_list = set(A)
bb_counter = collections.Counter()
#print(bb_counter)
for b in B:
    b_counter = collections.Counter(b)
#    print(b_counter)
    for b_key in b_counter.keys():
#        print(b_key)
        if b_counter[b_key]>bb_counter[b_key]:
            bb_counter[b_key]=b_counter[b_key]
for a in A:
    a_counter = collections.Counter(a)
    for bb in bb_counter.keys():
        if a_counter[bb]<bb_counter[bb]:
            ans_list.remove(a)
            break
print(list(ans_list))