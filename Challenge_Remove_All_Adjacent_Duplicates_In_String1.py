# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 18:14:55 2021

@author: ppj
"""

s = "abbaca"
stack=[]
for i in range(len(s)):
    if stack and stack[-1]==s[i]:
        stack.pop()
    else:
        stack.append(s[i])
print(''.join(stack))

#%%
s = "abbaca"

re=set([i*2 for i in s])

prev=-1
while prev!=len(s):
    prev=len(s)
    for r in re:
        #print(r)
        s=s.replace(r,'')
print(s)
    