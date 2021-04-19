# -*- coding: utf-8 -*-
# TLE
"""
Created on Fri Apr 16 15:16:30 2021

@author: ppj
"""

s = "pbbcggttciiippooaais"
k = 2
stack=[]
check=[]
for i in range(len(s)):
    stack.append(s[i])
    check=stack[-k:]
    while len(check)==k and len(set(check))==1:
        stack=stack[:-k]
        check=stack[-k:]
print(''.join(stack))
#%% TLE
import collections      
s = "pbbcggttciiippooaais"
k = 2
stack=[]
check=[]
for i in range(len(s)):
    stack.append(s[i])
    check=collections.Counter(stack[-k:])
    print(check)
#    check=stack[-k:]
    while len(stack[-k:])==k and list(check.values())[0]==k:
        stack=stack[:-k]
        check=collections.Counter(stack[-k:])
print(''.join(stack))
#%%
import collections      
s = "pbbcggttciiippooaais"
k = 2

stack=[]
ans=''
for i in range(len(s)):
#    print(i)
    if stack and s[i]==stack[-1][0]:
        stack[-1][1]+=1
        if stack[-1][1]==k:
            stack.pop()
    else:
        stack.append([s[i],1])
for i in stack:
    ans+=i[0]*i[1]
print(ans)
