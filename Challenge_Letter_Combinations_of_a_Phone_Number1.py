# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 12:28:44 2021

@author: ppj
"""

digits = "2399"
dig_dict={}
for i in range(2,7):
    dig_dict[str(i)]=list(map(chr,list(range(91+i*3,94+i*3))))
dig_dict['7']=['p','q','r','s']
dig_dict['8']=['t','u','v']
dig_dict['9']=['w','x','y','z']

if len(digits)==0:
    ans = []
elif len(digits)==1:
    ans = dig_dict[digits[0]]
elif len(digits)==2:
    ans = [a+b for a in dig_dict[digits[0]] for b in dig_dict[digits[1]]]
elif len(digits)==3:
    ans = [a+b+c for a in dig_dict[digits[0]] for b in dig_dict[digits[1]] for c in dig_dict[digits[2]]]
else:
    ans = [a+b+c+d for a in dig_dict[digits[0]] for b in dig_dict[digits[1]] for c in dig_dict[digits[2]] for d in dig_dict[digits[3]]]
print(ans)

#%%
digits = "23"
if digits == '':
    print ([])
dig_dict={}
for i in range(2,7):
    dig_dict[str(i)]=list(map(chr,list(range(91+i*3,94+i*3))))
dig_dict['7']=['p','q','r','s']
dig_dict['8']=['t','u','v']
dig_dict['9']=['w','x','y','z']
ans_ls=dig_dict[digits[0]]
ans=[]
for i in digits[1:]:
    ans_ls = [a+b for a in ans_ls for b in dig_dict[i]]
print(ans_ls)
