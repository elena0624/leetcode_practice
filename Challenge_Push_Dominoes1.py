# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 11:49:47 2021

@author: ppj
"""

dominoes = ".L.R...LR..L.."

dominoes=list(dominoes)
#%%

tmp_d=dominoes.copy()
# 往右看
for i in range(1,len(dominoes)):
    if dominoes[i]=='.' and tmp_d[i-1]=='R':
        tmp_d[i]='R'
# 往左看
for i in range(len(dominoes)-2,-1,-1):
    if tmp_d[i+1]=='L':
       # 如果本來是直的 就倒
       if tmp_d[i]=='.':
           tmp_d[i]='L'
       # 如果被網另外一邊推 反而變成正的 但要是原本是正的情況下
       elif tmp_d[i]=='R':
           tmp_d[i]='.'
#    dominoes[i]=='.' and 
#         tmp_d[i]='L'
#%%
dominoes = ".L.R...LR..L.."

dominoes=list(dominoes)

change=False
while not change:
    for i in range(len(dominoes)):
        tmp=dominoes.copy()
        # 推導的隔壁步
        # 如果右邊是L，那左邊的應該1.已經被往左 還是左 2.已經被往右 還是右 3.左邊是右 所以往右 此時不變 4.原本直 就往左
        if dominoes[i]=='L':
            #
            tmp[i-1]='L'
#%%
dominoes = ".L.R...LR..L.."
dominoes = ".R........"
dominoes=list(dominoes)

tmp=dominoes.copy()
# 每一步先檢查自己的左右邊
for i in range(len(dominoes)):
    # 會有幾種情況:
    # 如果自己本身已有方向 就不用考慮
    if dominoes[i]=='.':
        # 左非R右L>L
        if i<len(dominoes)-1 and (i==0 or dominoes[i-1]!='R') and dominoes[i+1]=='L':
            tmp[i]='L'
        # 左R右非L>R
        elif i>0 and dominoes[i-1]=='R' and (i==len(dominoes)-1 or dominoes[i+1]!='L'):
            tmp[i]='R'
    # 左.右.>.
    # 左R右L>.
# 這只有考慮到隔壁步，現在要繼續考慮，直到???=>直到兩輪下來結果相等 不再變化
while dominoes!=tmp:
    dominoes=tmp.copy()
#    print(dominoes)
#    print(tmp)
    for i in range(len(dominoes)):
        # 會有幾種情況:
        # 如果自己本身已有方向 就不用考慮
        if dominoes[i]=='.':
            # 左非R右L>L
            if i<len(dominoes)-1 and (i==0 or dominoes[i-1]!='R') and dominoes[i+1]=='L':
                tmp[i]='L'
            # 左R右非L>R
            elif i>0 and dominoes[i-1]=='R' and (i==len(dominoes)-1 or dominoes[i+1]!='L'):
                tmp[i]='R'
    # 左.右.>.
    # 左R右L>.
print(dominoes)
    
#%%
dominoes = ".L.R...LR..L.."

def cmp(a, b):
    return (a > b) - (a < b) 
symbols = [(i, x) for i, x in enumerate(dominoes) if x != '.']
symbols = [(-1, 'L')] + symbols + [(len(dominoes), 'R')]
#%%
ans = list(dominoes)
for (i, x), (j, y) in zip(symbols, symbols[1:]):
    print(i,x,j,y)
    if x == y:
        for k in range(i+1, j):
            ans[k] = x
    elif x > y: #RL
        for k in range(i+1, j):
            ans[k] = '.LR'[cmp(k-i, j-k)]

return "".join(ans)
