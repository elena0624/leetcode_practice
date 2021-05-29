# -*- coding: utf-8 -*-
"""
Created on Sat May 29 18:28:08 2021

@author: ppj
"""

#n=1
n=5

not_used=set(range(n))

col=set()
#row=set()
#row=set(range(n))
dia=set()
andia=set()

ans=0

#def dfs(ls,not_used,col,row,dia,andia,ans):
def dfs(ls,not_used,col,dia,andia,ans):
    if len(ls)==n:
        return ans+1
    for i in not_used:
        cur_not_used=not_used.copy()
        cur_col=i
#        cur_row=i
        cur_dia=i-(len(ls)+1)
        cur_andia=i+len(ls)+1
        if (cur_col not in col) and (cur_dia not in dia) and (cur_andia not in andia):# 如果可安全插入
            ls.append(i)
            col.add(cur_col)
            dia.add(cur_dia)
            andia.add(cur_andia)
            cur_not_used.remove(i)
            ans=dfs(ls,cur_not_used,col,dia,andia,ans)
            ls.pop()
            col.remove(cur_col)
            dia.remove(cur_dia)
            andia.remove(cur_andia)
    return ans
print(dfs([],not_used,col,dia,andia,ans))
