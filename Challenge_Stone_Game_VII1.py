# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 18:31:55 2021

@author: ppj
"""
#%% Incorrect. not greedy
stones = [5,3,1,4,2]

ans=0
l=0
r=len(stones)-1
dis=0
for i in range(len(stones)):
    if stones[l]<=stones[r]:#l比較小 移除l
        dis=stones[l]
        l+=1
    else:
        dis=stones[r]
        r-=1
    # 如果是bob才要加
    print(dis)
    if i%2==1:
        print('bob的',dis)
        ans+=dis 
print(ans)
#%%
#from functools import lru_cache
stones = [5,3,1,4,2]

#@lru_cache(maxsize=None)
def get_result(stones,a_idx):
    # 到剩下最後一個才能確定
    if len(stones)==1:
        if a_idx:
            return 0
        else:
            return stones[0]
    else:
        if a_idx:
            return max(get_result(stones[1:],not a_idx),get_result(stones[:-1],not a_idx))
        else:# bob的turn 要+他拿的
            return min(stones[0]+get_result(stones[1:],not a_idx),stones[-1]+get_result(stones[:-1],not a_idx))
print(get_result(stones, True))
#%% lru cache不能用list 改用tuple
# 結果還是超時了
from functools import lru_cache
stones = [5,3,1,4,2]
stones = [7,90,5,1,100,10,10,2]
@lru_cache(maxsize=None)
def get_result(stones,a_idx):
    # 到剩下最後一個才能確定
    if len(stones)==1:
        if a_idx:
            return 0
        else:
            return stones[0]
    else:
        if a_idx:
            return max(get_result(stones[1:],not a_idx),get_result(stones[:-1],not a_idx))
        else:# bob的turn 要+他拿的
            return min(stones[0]+get_result(stones[1:],not a_idx),stones[-1]+get_result(stones[:-1],not a_idx))
print(get_result(tuple(stones), True))
#%% 改成n^2
from functools import lru_cache
# 靠夭喔 阿不是說n^2可以
# 加了lru cache才可以 單個case
#import collections

stones = [5,3,1,4,2]
stones = [7,90,5,1,100,10,10,2]

#dp=collections.defaultdict(int)
dp=dict()
parity=len(stones)%2

l=0
stone_len=len(stones)

#奇數的話是alice拿最後一個 沒分
#偶數的話是bob拿最後一個 有分
@lru_cache(maxsize=None)
def get_result(l,stone_len):
    #如果存在
    if (l,stone_len) in dp:
        return dp[(l,stone_len)]    
    # 到剩下最後兩個可以確定 且最少兩個
    if stone_len==2:# 剩下兩個 如果是奇數就是輪到bob拿 最後一個留給alice 這時bob會拿比較小的
        if parity:
#            dp[(l,stone_len)]=min(stones[l],stones[l+1])
            dp[(l,stone_len)]=stones[l] if stones[l]<stones[l+1] else stones[l+1]
        else:# 剩下兩個 如果是偶數就是輪到alice拿 最後一個留給bob 這時alice也會拿比較小的 留給bob比較大的
#            dp[(l,stone_len)]=max(stones[l],stones[l+1])
            dp[(l,stone_len)]=stones[l] if stones[l]>stones[l+1] else stones[l+1]
        return dp[(l,stone_len)]
    else: # 剩三個以上，就是比較拿掉哪個之後會比較好
        if stone_len%2+parity!=1:#現在剩下的跟原始同機偶性=>是alice拿
            return max(get_result(l,stone_len-1),get_result(l+1,stone_len-1))
        else:# bob的turn 要+他拿的
            return min(get_result(l,stone_len-1)+stones[l+stone_len-1],get_result(l+1,stone_len-1)+stones[l])
print(get_result(l,stone_len))
#%% 修改一下下
from functools import lru_cache
# 加了lru cache才可以 單個case
#import collections

stones = [5,3,1,4,2]
stones = [7,90,5,1,100,10,10,2]

#dp=collections.defaultdict(int)
dp=dict()
parity=len(stones)%2

l=0
stone_len=len(stones)

#奇數的話是alice拿最後一個 沒分
#偶數的話是bob拿最後一個 有分
@lru_cache(maxsize=None)
def get_result(l,stone_len):
    #如果存在
    if (l,stone_len) in dp:
        return dp[(l,stone_len)]
    if stone_len==1:
        dp[(l,stone_len)]=stones[l] if parity==0 else 0
        return dp[(l,stone_len)]
    else: # 剩三個以上，就是比較拿掉哪個之後會比較好
        if stone_len%2+parity!=1:#現在剩下的跟原始同機偶性=>是alice拿
            return max(get_result(l,stone_len-1),get_result(l+1,stone_len-1))
        else:# bob的turn 要+他拿的
            return min(get_result(l,stone_len-1)+stones[l+stone_len-1],get_result(l+1,stone_len-1)+stones[l])
print(get_result(l,stone_len))


#%% ACCEPTED!!!!
stones = [5,3,1,4,2]
stones = [7,90,5,1,100,10,10,2]

#dp=collections.defaultdict(int)
n=len(stones)
dp=[[None for i in range(n+1)] for j in range(n+1)]
parity=len(stones)%2

for i in range(1,n+1):#長度
    for l in range(n-i+1):#起點
#        print(i)
#        print(l)
        if i==1:
            dp[1][l]=stones[l] if parity==0 else 0
        else:
            if i%2+parity!=1:#alice拿
                dp[i][l]=max(dp[i-1][l],dp[i-1][l+1])
            else:# bob拿
                dp[i][l]=min(dp[i-1][l]+stones[l+i-1],dp[i-1][l+1]+stones[l])
print(dp[n][0])
                