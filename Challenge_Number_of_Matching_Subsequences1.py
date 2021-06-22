# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 01:44:32 2021

@author: ppj
"""

s = "abcde"
words = ["a","bb","acd","ace"]

s = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]

import collections

s_dict = collections.defaultdict(list)

for i in range(len(s)):
    s_dict[s[i]].append(i)


ans=len(words)
for i in words:# n
    a=-1
    for j in i: # n
        if s_dict[j]==[]:
            ans-=1
            break
        else:
            exist=False
            for k in s_dict[j]:# a
                if k>a:
                    a=k
                    exist=True
                    break
            if exist==False:
                ans-=1
                break
    
print(ans)
                    
            