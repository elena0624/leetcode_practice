# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 14:11:45 2021

@author: ppj
"""

import collections

order = "cba"
s = "abcd"

ans=""
dic_s = collections.Counter(s)
ls=list(dic_s.keys())

for i in order:
    ans+=i*dic_s[i]
    if i in ls:
        ls.remove(i) 
for j in ls:
    ans+=j*dic_s[j]
print(ans)

