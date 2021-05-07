# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:48:05 2021

@author: ppj
"""
import collections
word1 = "sea"
word2 = "eat"
#word1 = "leetcode"
#word2 = "etco"
#word1 = "a"
#word2 = "b"
word1="leetcode"
word2="test"
w1_dict=collections.defaultdict(list)
for i in range(len(word1)):
    w1_dict[word1[i]].append(i)
w2_ls=[]
for i in range(len(word2)):
    w2_ls.extend(w1_dict[word2[i]][::-1])
if not w2_ls:
    print(len(word1)+len(word2))
# 參考300題
ans_ls=[w2_ls[0]]

for i in range(1,len(w2_ls)):
    print(ans_ls)
    if w2_ls[i]>ans_ls[-1]:
        ans_ls.append(w2_ls[i])
    elif w2_ls[i]<ans_ls[0]:
        ans_ls[0]=w2_ls[i]
    elif w2_ls[i] in ans_ls:
        continue
    else:
        l=0
        r=len(ans_ls)-1
        while l<r:
            m=(l+r)//2
            if w2_ls[i]>ans_ls[m]:# >m，因為找找比x大的，m也不用考慮了
                l=m+1
            else:#<m 因為要找比x大的,所以m也要考慮
                r=m
        ans_ls[r]=w2_ls[i]
# 共同最長是len(ans_ls)
        
print(len(word1)+len(word2)-2*len(ans_ls))
#%%
import collections
import bisect
word1 = "sea"
word2 = "eat"
#word1 = "leetcode"
#word2 = "etco"
#word1 = "a"
#word2 = "b"
word1="leetcode"
word2="test"
w1_dict=collections.defaultdict(list)
for i in range(len(word1)):
    w1_dict[word1[i]].append(i)
w2_ls=[]
for i in range(len(word2)):
    w2_ls.extend(w1_dict[word2[i]][::-1])
if not w2_ls:
    print(len(word1)+len(word2))
# 參考300題
ans_ls=[w2_ls[0]]

for i in range(1,len(w2_ls)):
    print(ans_ls)
    if w2_ls[i]>ans_ls[-1]:
        ans_ls.append(w2_ls[i])
    else:
        ans_ls[bisect.bisect_left(ans_ls,w2_ls[i])]=w2_ls[i]
# 共同最長是len(ans_ls)
        
print(len(word1)+len(word2)-2*len(ans_ls))