# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 17:52:21 2021

@author: ppj
"""
#%%
#s = "bababc"

#s = "cbbd"

#s = "a"

#s = "ac"

s = "caba"

# 先檢查如果完全一樣就直接return
if s==s[::-1]:
    print(s)
    print('跳出')
str_len = 1 # 
odd_idx = [*range(len(s))] # or list(range(len(s)) # 所有都是 # 最新
odd_idx_new = odd_idx.copy()# 當前

str_len = 2
even_idx = []
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        even_idx.append(i)
even_idx_new = even_idx.copy()

# n從0開始到最大，如果中間已經沒有了就結束
# n直接改成str_len
for str_len in range(3,(len(s)+1)):#從3開始因為其他前面先初始化過了
    print(str_len)
    print('odd_idx',odd_idx)
    print('even_idx',even_idx)
    print('odd_idx_new',odd_idx_new)
    print('even_idx_new',even_idx_new)

    if str_len%2 == 1:    # 奇數情形
        # 如果前一輪還有
        if odd_idx_new:
            print('here')
            odd_idx = odd_idx_new.copy() # 直接拿掉也可以
            odd_idx_new = []
            print('odd_idx',odd_idx)
            print('odd_idx_new',odd_idx_new)
            for idx in odd_idx:
                print('idx',idx)
                if idx-1<0:#太小了不行 下一個
                    print('continue')
                    continue
                elif idx+str_len-2>len(s)-1:#太大了不行 這輪end
                    print('elif')
                    break
                elif s[idx-1]==s[idx+str_len-2]:
                    odd_idx_new.append(idx-1)# idx 紀錄起始位置
                    print('odd_idx_new',odd_idx_new)
    else: #偶數情形
        # 如果前一輪還有
        if even_idx_new:
            even_idx = even_idx_new.copy() # 直接拿掉也可以
            even_idx_new = []
            for idx in even_idx:
                if idx-1<0:#太小了不行 下一個
                    continue
                elif idx+str_len-2>len(s)-1:#太大了不行 這輪end
                    break
                elif s[idx-1]==s[idx+str_len-2]:
                    even_idx_new.append(idx-1)# i 紀錄起始位置
      
    # 如果都沒有新的了
    if (not(odd_idx_new) and not(even_idx_new)):
        str_len = str_len-2
        if str_len%2==1:
            print( s[odd_idx[0]:odd_idx[0]+str_len])
            print('跳出')
        else:
            print( s[even_idx[0]:even_idx[0]+str_len])
            print('跳出')
# 如果執行到最後odd或even的new裡還有東西=>完全相等的情況被排除了，所以是n-1裡面有東西
str_len -= 1
if str_len%2==1:
    print( s[odd_idx_new[0]:odd_idx_new[0]+str_len])
else:
    print( s[even_idx_new[0]:even_idx_new[0]+str_len])
print('跳出')

#%% 想辦法簡化一下
# 待努力...
# 3/28 updated,套用	Palindromic Substrings解法的概念試試看
#s = "bababc"

#s = "cbbd"

#s = "a"

#s = "ac"

s = "caaba"
i=0
all_long_len=1
all_l=0
while i<len(s):
    print('i',i)
    cur_long_len=1
    r=i
    l=i
    while (r<len(s)-1 and s[r]==s[r+1]):
        r+=1
        cur_long_len+=1
    i=r+1
    print('i',i)
    print('l',l)
    print('r',r)
    print('cur_long_len',cur_long_len)
    while (l>0 and r<len(s)-1 and s[l-1]==s[r+1]):
        print('l',l,'r',r)
        print('s[l-1]',s[l-1],'s[r+1]',s[r+1])
        l-=1
        r+=1
        cur_long_len+=2
    print('cur_long_len',cur_long_len)
    print('all_long_len',all_long_len)
    if cur_long_len>all_long_len:
        all_long_len=cur_long_len
        all_l=l
    
print(s[all_l:all_l+all_long_len])
        
        