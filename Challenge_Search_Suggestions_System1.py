# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 12:58:11 2021

@author: ppj
"""
# Failed
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

# 建立Tree
class TrieNode:
    def __init__(self):
        self.isWord=False
        self.child={}

cur=root=TrieNode()
for i in products:
    cur=root
    for j in i:
        if j not in cur.child:
            cur.child[j]=TrieNode()
        cur=cur.child[j]
    cur.isWord=True
#        print(j,ord(j)-97)
    

def findprefix(s,cur):
    for i in s:
        if i in cur.child:
            cur=cur.child[i]
        else:
            return False  
    return cur
def preordersearch(s, pre_cur, ans):
    if len(ans)==3:
        return ans
    if pre_cur.isWord:
        ans.append(s)
    for i in sorted(pre_cur.child):
        preordersearch(s+i,pre_cur.child[i],ans)
    return ans
        
ans=[]
cur=root
for i in range(1,len(searchWord)+1):# 針對每鑑入
    cur_n=findprefix(searchWord[:i],cur)
    if cur_n:
        ans.append(preordersearch(searchWord[:i],cur_n,[]))
    else:
        ans.append([])
print(ans)

        
#%% Brute Force


products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
products = ["havana"]
searchWord = "tatiana"

products = sorted(products)
ans=[]
for i in range(1,len(searchWord)+1):
    ans_tp=[]
    for product in products:
        if product[:i]==searchWord[:i]:
            ans_tp.append(product)
    ans.append(ans_tp[:3])
#%% bisect  => built-in
import bisect
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
#products = ["havana"]
#searchWord = "tatiana"

products = sorted(products)
ans=[]

for i in range(1,len(searchWord)+1):
    j=bisect.bisect_left(products,searchWord[:i])
    print('j',j)
    ans.append([products[k] for k in range(j,j+3) if k<len(products) and products[k][:i]==searchWord[:i]])
print(ans)
#%%

products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"
#products = ["havana"]
#searchWord = "tatiana"

products = sorted(products)
ans=[]

def bisect(sw):
    l=0
    r=len(products)-1
    while l<r:
        m=(l+r)//2
        if sw>products[m]:# 如果位在左邊
            l=m+1
        else: #位在右邊
            r=m
    return r

for i in range(1,len(searchWord)+1):
#    j=bisect.bisect_left(products,searchWord[:i])
    j=bisect(searchWord[:i])
#    print('j',j) 
    ans.append([products[k] for k in range(j,j+3) if k<len(products) and products[k][:i]==searchWord[:i]])
print(ans)

#%% 2 pointers
products = ["mobile","mouse","moneypot","monitor","mousepad"]
searchWord = "mouse"

n = len(products)
products.sort()  # Sort by increasing lexicographically order of products
ans = []
startIndex, endIndex = 0, n - 1
for i, c in enumerate(searchWord):
#    print('i',i)
#    print('c',c)
    while startIndex <= endIndex and (i >= len(products[startIndex]) or products[startIndex][i] < c):
        startIndex += 1
    while startIndex <= endIndex and (i >= len(products[endIndex]) or products[endIndex][i] > c):
        endIndex -= 1

    suggestProducts = []
    for j in range(startIndex, min(startIndex+3, endIndex+1)):
        suggestProducts.append(products[j])
    ans.append(suggestProducts)

