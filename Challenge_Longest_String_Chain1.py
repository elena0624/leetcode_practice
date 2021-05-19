# -*- coding: utf-8 -*-
"""
Created on Tue May 18 03:00:39 2021

@author: ppj
"""

import collections

words = ["a","b","ba","bca","bda","bdca"]

words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]


words = sorted(words, key=lambda x:len(x), reverse=True)

#memo = [0 for i in range(len(words))]
memo = collections.defaultdict(int)

def check_pre(cur_str):
    if memo[cur_str]:
        return memo[cur_str]
    stack=[]
    remove_chr = [cur_str[:k-1]+cur_str[k:] for k in range(1,len(cur_str))]+[cur_str[1:],cur_str[:-1]]
    for i in range(len(words)):
#        if len(words[i])==len(cur_str)-1 and words[i] in cur_str:
#        if len(words[i])==len(cur_str)-1 and (words[i] in [cur_str[:k-1]+cur_str[k:] for k in range(1,len(cur_str))] or words[i] in cur_str):
        if len(words[i])==len(cur_str)-1 and (words[i] in remove_chr):
            stack.append(words[i])
        elif len(words[i])<len(cur_str)-1:
            break
        
    if not stack:
        memo[cur_str]=1
        return(1)
    else:
        max_step=0        
        for i in stack:
#            cur_step = check_pre(i,step+1)
            cur_step = check_pre(i)+1
            max_step=max(max_step,cur_step)
        memo[cur_str]=max_step
        return max_step

ans= 0
for i in range(len(words)):
    check_pre(words[i])
    ans=max(memo[words[i]],ans)
    
#print(memo)
print(ans)
#%%
import collections

words = ["a","b","ba","bca","bda","bdca"]
words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]

words = sorted(words, key=lambda x:len(x), reverse=True)

#memo = [0 for i in range(len(words))]
memo = collections.defaultdict(int)

def check_pre(cur_str):
    if memo[cur_str]:
        return memo[cur_str]
    remove_chr = [cur_str[:k-1]+cur_str[k:] for k in range(1,len(cur_str))]+[cur_str[:-1]]
    max_step=1
    for i in range(len(words)):
        if words[i] in remove_chr:
            cur_step = check_pre(words[i])+1
            max_step=max(max_step,cur_step)
    memo[cur_str]=max_step
    return max_step

ans= 0
for i in range(len(words)):
    check_pre(words[i])
    ans=max(memo[words[i]],ans)
    
print(ans)
#%%
import collections

#words = ["a","b","ba","bca","bda","bdca"]
words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]

words = sorted(words, key=lambda x:len(x))

memo = collections.defaultdict(int)

ans=0
for i in range(len(words)):
    cur_longest=1
#    print(words[i])
    remove_chr = [words[i][:k-1]+words[i][k:] for k in range(1,len(words[i]))]+[words[i][:-1]]
#    print(remove_chr)
    for j in remove_chr:
        if memo[j]:
            cur_longest=max(cur_longest,memo[j]+1)
    memo[words[i]]=cur_longest
    ans=max(ans,cur_longest)
print(ans)