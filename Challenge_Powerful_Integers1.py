# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 22:13:08 2021

@author: ppj
"""

x = 2
y = 1
bound = 10
ans=set()
a=0
b=0
while x**a+y**b<=bound:
    print('a',a)
    while x**a+y**b<=bound:
        ans.add(x**a+y**b)
        print(ans)
        print('b',b)
        print(x**a+y**b)
        if y!=1:
            b+=1
        else:
            break
    b=0
    if x!=1:
        a+=1
    else:
        break
print(list(ans))
