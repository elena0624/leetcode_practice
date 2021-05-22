# -*- coding: utf-8 -*-
"""
Created on Sat May 22 16:25:16 2021

@author: ppj
"""
#%% Wrong
n=4
n=5
# 先建立Qlist
#ini_row = ["."*n for j in range(n)]
ans=[]
ini_row = ["" for j in range(n)]
for i in range(n):
    for j in range(n):
        ini_row[i]+="." if j!=i else "Q"
#再來看每行該怎麼排列
if n==1:
    print(ini_row)
elif n==2 or n==3:
    print("")
elif n==4:
    print([[ini_row[1],ini_row[3],ini_row[0],ini_row[2]],[ini_row[2],ini_row[0],ini_row[3],ini_row[1]]])
else:
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(ini_row[(i+2*j)%n])
        ans.append(row)  
#%% Brute Force
n=4
n=6
# 先建立Qlist
#ini_row = ["."*n for j in range(n)]
ans=[]
ini_row = ["" for j in range(n)]
for i in range(n):
    for j in range(n):
        ini_row[i]+="." if j!=i else "Q"


used=set()
def dfs(cur,used):
#    print(cur,used)
    tl = len(cur) if cur else 0
    if tl==n:
        return cur
    for j in range(n):
#        print('j',j)
        if j not in used:
            temp_sig=True
            # 要加上去的話要檢查左上 右上(上不用因為只有一個)
            for k in range(len(cur)):
                if (j-(tl-k)>=0 and cur[k][j-(tl-k)]=='Q') or (j+(tl-k)<(n) and cur[k][j+(tl-k)]=='Q'):# 如果有衝突就不行
                    temp_sig=False
                    break
            if temp_sig:
                cur_new = cur.copy()
                cur_new.append(ini_row[j])
                used_new = used.copy()
                used_new.add(j)
#                print('here',)
                ans.append(dfs(cur_new,used_new))
dfs([],used)
#print(ans)
print(list(filter(None, ans)))
#%% 稍微修改
n=4
n=6
# 先建立Qlist
#ini_row = ["."*n for j in range(n)]
ans=[]
ini_row = ["" for j in range(n)]
for i in range(n):
    for j in range(n):
        ini_row[i]+="." if j!=i else "Q"


used=set()
def dfs(cur,used):
#    print(cur,used)
    tl = len(cur)
    if tl==n:
        ans.append(cur)
        return
    for j in range(n):
#        print('j',j)
        if j not in used:
            temp_sig=True
            # 要加上去的話要檢查左上 右上(上不用因為只有一個)
            for k in range(len(cur)):
                if (j-(tl-k)>=0 and cur[k][j-(tl-k)]=='Q') or (j+(tl-k)<(n) and cur[k][j+(tl-k)]=='Q'):# 如果有衝突就不行
                    temp_sig=False
                    break
            if temp_sig:
                cur_new = cur.copy()
                cur_new.append(ini_row[j])
                used_new = used.copy()
                used_new.add(j)
#                print('here',)
                dfs(cur_new,used_new)
dfs([],used)
print(ans)
#%%
n=4
n=6
# 先建立Qlist
#ini_row = ["."*n for j in range(n)]
ans=[]
ini_row = ["" for j in range(n)]
for i in range(n):
    for j in range(n):
        ini_row[i]+="." if j!=i else "Q"


used=set()
diag=set()
andiag=set()
def dfs(cur,used,diag,andiag):
    tl = len(cur)
    if tl==n:
        ans.append(cur)
        return
    for j in range(n):
        diag_cur = j-tl
        andiag_cur = j+tl
        if j not in used and diag_cur not in diag and andiag_cur not in andiag:
            cur_new = cur.copy()
            cur_new.append(ini_row[j])
            used_new = used.copy()
            used_new.add(j)
            diag_new = diag.copy()
            diag_new.add(diag_cur)
            andiag_new = andiag.copy()
            andiag_new.add(andiag_cur)
            dfs(cur_new,used_new,diag_new,andiag_new)
dfs([],used,diag,andiag)
print(ans)
