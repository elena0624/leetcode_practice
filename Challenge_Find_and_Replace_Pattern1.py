# -*- coding: utf-8 -*-
"""
Created on Fri May 21 17:38:25 2021

@author: ppj
"""

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
words = ["a","b","c"]
pattern = "a"

ans=words.copy()
#ans = [True for i in words]
for i in range(len(words)):
    biject=dict()
    used=set()
    for j in range(len(words[i])):
        if words[i][j] in biject and biject[words[i][j]] == pattern[j]:
            continue
        elif words[i][j] not in biject and pattern[j] not in used:
            biject[words[i][j]] = pattern[j]
            used.add(pattern[j])
        else:
            ans.remove(words[i])
            break
        
#            ans[i]=False
print(ans)
        