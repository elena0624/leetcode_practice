# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 12:09:22 2021

@author: ppj
"""

s="00110011"
s="10101"
s="1"
i=0
ans=0
while (i+1)<len(s):
    if s[i]!=s[i+1]:
        ans+=1
        l=i
        r=i+1
        while l>0 and (r+1)<len(s) and s[l-1]==s[l] and s[r+1]==s[r]:
            print(s[(l-1):(r+2)])
            ans+=1
            l-=1
            r+=1
        i=r
    else:
        i+=1
print(ans)

#%% Group by 

s="00110011"
s="1"
groups=[1]
for i in range(1,len(s)):
    print(i)
    if s[i]!=s[i-1]:
        groups.append(1)
    else:
        groups[-1]+=1
print(groups)
ans=0
for i in range(len(groups)-1):
    ans+=min(groups[i],groups[i+1])
print(ans)

#%%
s="0110110011"
#s="00110011"
#s="1"

prev=0
cur=1
ans=0
for i in range(1,len(s)):
    print(i)
    if s[i-1]!=s[i]:
        ans+=min(prev,cur)
        prev=cur
        cur=1
    else:
        cur+=1
    print('prev',prev)
    print('cur',cur)
    print('ans',ans)
ans+=min(prev,cur)
print(ans)
