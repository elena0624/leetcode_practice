# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 11:59:14 2021

@author: ppj
"""

n=6
ls=[[1]]
if n==1:
    print(ls)
ls.append([1,1])
if n==2:
    print(ls)
for i in range(2,n):
    new_ls=[1]
    for j in range(1,i//2+1):
        # 如果i是偶數就是奇數個 到//2就翻轉
        # 如果i是奇數就是偶數個 +1//2翻轉除了中間的那個
        # 所以都是到//2+1翻轉 只是翻轉的數量不同
        new_ls.append(ls[i-1][j-1]+ls[i-1][j])
    if i%2==1:
        new_ls = new_ls+new_ls[::-1]
    else:
        new_ls = new_ls+new_ls[-2::-1]
            
    ls.append(new_ls)
print(ls)
        
        
        
        #%%