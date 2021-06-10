# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 00:17:38 2021

@author: ppj
"""
import bisect
a=[]
start=37
end=50

#%%
def insert_ls(a,start,end):
    x = bisect.bisect(a, (start,end))
    print(x)
    if x>0 and a[x-1][0]==start:# 如果有重複的 insert的位置會是重複的下一個 所以看前面那個是不是一樣 一樣不行 start不能重複
        print(False)
        return a
    if x>0 and a[x-1][1]>start:# 如果這不是第一個 那前面那個end不能比這個start晚
        print(False)
        return a
    if x<len(a) and a[x][0]<end:# 如果這不是最後一個 那後面的start不能比這個end還早
        print(False)
        return a
    #else:# 可以 那就輸入
    a=a[:x]+[(start,end)]+a[x:]
    print(True)
    return a

#%%
a=insert_ls(a,37,50)
#%%
a=insert_ls(a,33,50)
#%%
a=insert_ls(a,32,42)


#%%
class MyCalendar:
    def __init__(self):
        self.intervals = []
    
    def book(self, start: int, end: int) -> bool:
        if end <= start:
            return False
        i = bisect.bisect_right(self.intervals, start)
        if i % 2:            # start is in some stored interval
            return False
        j = bisect.bisect_left(self.intervals, end)
        if i != j:
            return False
        self.intervals[i:i] = [start, end]
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
#%%
def insert_ls(s_l,e_l,start,end):
    # bisect
    # 把start跟end去比
    l=0
    r=len(e_l)
    while l<r:
        m=(l+r)//2
        if start>=e_l[m]:
            l=m+1
        else:
            r=m
    #print(r)
#    print(max(r,l))
    if r==len(e_l) or s_l[r]>=end:
        s_l.insert(r,start)
        e_l.insert(r,end)
        print(True)
    else:
        print(False)
    return s_l,e_l
#%%
s_l=[]
e_l=[]
s_l,e_l = insert_ls(s_l,e_l,10,20)
#%%
s_l,e_l = insert_ls(s_l,e_l,15,25)
#%%
s_l,e_l = insert_ls(s_l,e_l,20,30)