# -*- coding: utf-8 -*-
"""
Created on Thu May 13 16:08:06 2021

@author: ppj
"""

s = "(123)"
s = "(00011)"
s = "(0123)"
#s = "(100)"
s="(0010)"
print(s[2:-2])

def possible_comb(s):
    s_ls = []
    if len(s)==1:
#        print('[s]',s)
        return [s]
    if s.count('0')==len(s) or s[0]==s[-1]=='0':
#        print('False')
        return False
    if s[-1]=='0':
#        print('[s]',s)
        return [s]

    if s[0]=='0':
#        print("[s[0]+'.'+s[1:]]",[s[0]+'.'+s[1:]])
        return [s[0]+'.'+s[1:]]
    else:
        for i in range(len(s)-1):
#            s_ls.append(s[:i+1]+'.'+s[i+1:])
#            '%g'%(3.140)
            s_ls.append(s[:i+1]+'.'+s[i+1:])
#        print('s_ls',s_ls)
        s_ls.append(s)
        return s_ls
ans_ls=[]
for i in range(2,2+len(s[2:-1])):
    print('s1',s[1:i],'s2',s[i:-1])
    s1 = possible_comb(s[1:i])
    s2 = possible_comb(s[i:-1])
    if s1 and s2:
        ans_ls.extend(['('+a+', '+b+')' for a in s1 for b in s2])
print(ans_ls)