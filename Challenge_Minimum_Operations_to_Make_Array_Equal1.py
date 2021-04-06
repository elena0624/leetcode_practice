# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 16:18:38 2021

@author: ppj
"""

n=3
if n%2==1:
    ans= (((n-1)//2)*2)*(n+1)//2//2
else:
    ans=(1+(n//2)*2-1)*n//2//2
print(ans)