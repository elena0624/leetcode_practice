# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 10:37:49 2021

@author: ppj
"""

word = "a123bc34d8ef34"
#"leet1234code234"
#"a1b01c001"

#import collections
import string
#print(collections.Counter(string.ascii_lowercase))
word2= ''
for i in range (len(word)):
    if word[i] in string.ascii_lowercase:
        word2+=' '
    else:
        word2+=word[i]
#print(int())
print(len(set(list(map(int,word2.split())))))
#%%
# Revised after contest
word = "a123bc34d8ef34"
#"leet1234code234"
#"a1b01c001"
#ans=[] # =>最後用set的len，所以也不用用list，直接用set來存比較快
ans = set()
i=0
while i < (len(word)):
    print('i',i)
    if word[i].isdigit():
        print(word[i])
        l=i
        while l <len(word) and word[l].isdigit():
            l+=1
#            if word[l].isdigit() and l<len(word):# #是digitf且不是最後一個所以繼續找 #不用分這麼多層!!
#                l+=1# 是digit那就繼續找
#            else:
        ans.add(int(word[i:l]))
        i=l+1
    else:
        i+=1
print((ans))
print(len(ans))
    
#%%
n=4
perm = list(range(n))
print(perm)
arr = perm.copy()
s=1

equal_list = True
for i in range(n):
    print(i)
    if i % 2 == 0:
        arr[i] = perm[int(i / 2)]
    else:
        arr[i] = perm[int(n / 2 + (i - 1) / 2)]
    if arr[i] != perm[i]:
        equal_list = False
print(arr)
if equal_list:
    print('the same',s)

new_arr = arr.copy()

while True:
    s+=1
    print(s)
    equal_list = True
    for i in range(n):
        print(i)
        if i % 2 == 0:
            new_arr[i] = arr[int(i / 2)]
        else:
            new_arr[i] = arr[int(n / 2 + (i - 1) / 2)]
        if new_arr[i] != perm[i]:
            equal_list = False
    print('new_arr',new_arr)
    print('arr',arr)
    if equal_list:
        print('the same',s)
        break
    arr = new_arr.copy()
#%%
# revised after contest
n=4
perm = list(range(n))
arr = perm.copy()
s=0
while True:
    s+=1
    print(s)
    print(arr)
    arr = [arr[i//2] if i%2==0 else arr[n//2 + (i-1)//2] for i in range(n)]
    if arr == perm:
        print('the same',s)
        break

#%%

s= "(name)is(age)yearsold"
knowledge = [["name","bob"],["age","two"]]

s='c'
knowledge = []

#"hi(name)"
#[["a","b"]]
#"(a)(a)(a)aaa"
#[["a","yes"]]
#"(a)(b)"
#[["a","b"],["b","a"]]

knowledge_dict = {}
for i in range(len(knowledge)):
    knowledge_dict.setdefault(knowledge[i][0],knowledge[i][1])
print(knowledge_dict)
c_loc1=[]
c_loc2=[]
for i, c in enumerate(s):
        if c == '(':
            c_loc1.append(i)
        elif c == ')':
            c_loc2.append(i)
if not c_loc1:
    print(s)
temp_list = list(zip(c_loc1,c_loc2))
temp_list = list(map(list, temp_list))
print(temp_list)
s2 = s[0:temp_list[0][0]] 
print(s2)
for i in range(len(temp_list)-1):
    s2+=knowledge_dict.get(s[temp_list[i][0]+1:temp_list[i][1]], "?")
    s2+=s[temp_list[i][1]+1:temp_list[i+1][0]]
    print(s2)
s2+=knowledge_dict.get(s[temp_list[-1][0]+1:temp_list[-1][1]], "?")
s2+=s[temp_list[-1][1]+1:] 
print(s2)
#%%
# revised after contest
s= "(name)is(age)yearsold"
knowledge = [["name","bob"],["age","two"]]
#
#s='c'
#knowledge = []

knowledge_dict = {}
for k,v in knowledge:
#    print('k',k,'v',v)
    knowledge_dict[k]=v
i=0
ans=''
while i<len(s):
    if s[i]=='(':
        l=i+1
        while l<len(s) and s[l]!=')':
            l+=1
        ans+=knowledge_dict.get(s[i+1:l], "?")
        i=l+1
    else:
        ans+=s[i]
        i+=1
print(ans)
        

#%%
primeFactors = 8
mod = 10**9+7
if primeFactors ==1:
    print(1)
elif primeFactors%3==0:
    print(3**(primeFactors//3)%mod)
elif primeFactors%3==1:
    num3=(primeFactors-1)//3-1# 3n+1要拆成3m+2k=>3(n-1)+4=3(n-1)+2x2
    num2=2
    print((3**num3)*4%mod)
elif primeFactors%3==2:
    num3=(primeFactors-2)//3# 3n+1要拆成3m+2k=>3(n-1)+4=3(n-1)+2x2
    print((3**num3)*2%mod)
# =>TLE
#%%
primeFactors = 8
mod = 10**9+7
if primeFactors ==1:
    print(1)
elif primeFactors%3==0:
    print(pow(3,(primeFactors//3),mod))
elif primeFactors%3==1:
    num3=(primeFactors-1)//3-1# 3n+1要拆成3m+2k=>3(n-1)+4=3(n-1)+2x2
    num2=2
    print((pow(3,num3,mod)*4)%mod)# 注意,還要再mod一次
elif primeFactors%3==2:
    num3=(primeFactors-2)//3# 3n+1要拆成3m+2k=>3(n-1)+4=3(n-1)+2x2
    print((pow(3,num3,mod)*2)%mod)# 注意,還要再mod一次