# -*- coding: utf-8 -*-
"""
Created on Wed May 26 17:19:18 2021

@author: ppj
"""

words = ["abcw","baz","foo","bar","xtfn","abcdef"]

words = sorted(words,key = lambda x:len(x), reverse=True)

max_len=0

for i in range(len(words)):
    a_len=len(words[i])
    a_set=set(words[i])
    if a_len*a_len<=max_len:# 稍微剪枝
        break
    for j in range(i+1,len(words)):
        b_len=len(words[j])
        if b_len<=(max_len//a_len):# 稍微剪枝
            break
        if a_set.isdisjoint(set(words[j])):
            max_len=max(max_len,a_len*b_len)
print(max_len)

#%%
import itertools
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
d = {sum(1 << (ord(c) - 97) for c in set(w)): len(w) for w in sorted(words, key=len)}
print(max([d[k] * d[K] for k, K in itertools.combinations(d.keys(), 2) if not K & k] or [0]))
#%%
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
d = {}
for w in words:
    mask = 0
    for c in set(w):
        print('c',c)
        mask |= (1 << (ord(c) - 97))
        print('mask',mask)
    d[mask] = max(d.get(mask, 0), len(w))
print(max([d[x] * d[y] for x in d for y in d if not x & y] or [0]))


