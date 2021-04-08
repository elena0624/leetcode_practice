# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 22:34:14 2021

@author: ppj
"""

# 
import string
le_dic={}
for i,le in enumerate(list(string.ascii_lowercase[:9])):
#    print(i)
#    print(le)
    le_dic[le]=i
coordinates = "c7"
print(le_dic[coordinates[0]])
print(int(coordinates[1])%2)
if ((le_dic[coordinates[0]])%2+(int(coordinates[1]))%2)==1:
    print(False)
else:
    print(True)
#%%
sentence1 = "My name is Haley"
sentence2 = "My Haley"
#sentence1 = "of"
#sentence2 = "A lot of words"
#sentence1 = "Eating right now"
#sentence2 = "Eating"
#sentence1 = "Luky  Lucccky"
#sentence2 = "Lucccky"
#sentence1 = "Yo yo"
#sentence2 = "Hey hey"
#sentence1 = "CwFfRo regR"
#sentence2 = "CwFfRo H regR"
if sentence1==sentence2:
    print(True)

# 若長的頭=短的頭 長的尾=短的尾就可以 但是頭尾要從哪裡切?
# 都先切成words
ls_list = sentence1.split()
ss_list = sentence2.split()

if len(ls_list)==len(ss_list) and ls_list!=ss_list:
    print(False)
    
# 先比誰比較長
if len(ls_list)>=len(ss_list):
    ls_list,ss_list = ls_list,ss_list
else:
    ls_list,ss_list = ss_list,ls_list
    
# 比對頭
for i in range(len(ss_list)):
    if ls_list[i]==ss_list[i]:
        continue
    else:
        break
# 前半段完全一樣
if ls_list[:i+1]==ss_list:
    print(True, "結數")
# 代表~i-1是一樣的
# 比對尾
for j in range(len(ss_list)):
    if ls_list[-1-j]==ss_list[-1-j]:
        continue
    else:
        break
# 後半段完全一樣
if ls_list[-1-j:]==ss_list:
    print(True, "結數")

# 代表-j+1到最後一個是一樣的
# 若完全步一樣就是0 完全一樣就是?
print(i+j)

if (i+j)==len(ss_list):
    print(True)
else:
    print(False)
    
#%%
nums = [42,11,1,97,120]
nums = [13,10,35,24,76]
rev_ls = []
for i in nums:
    rev_ls.append(int(str(i)[::-1]))
print(rev_ls)
ans=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+rev_ls[j] == nums[j]+rev_ls[i]:
            ans+=1
print(ans)
#=>結果TLE
# 改成2SUM概念 用DIC存
#%%
import collections
#nums = [42,11,1,97,120]
nums = [13,10,35,24,76]
mod = 10**9+7
#rev_dic = {}
#for i in nums:
#    rev_dic[int(str(i)[::-1])] = i
#print(rev_dic)

rev_ls = []
for i in nums:
    rev_ls.append(int(str(i)[::-1]))
    
diff = []
for i in range(len(nums)):
    diff.append(rev_ls[i]-nums[i])

ans=0
temppp = list((collections.Counter(diff)).values())
for i in temppp:
    if i>1:
        ans+=(i*(i-1)//2)
        
print(int(ans%mod))

#%%
import math
batchSize = 4
groups = [1,3,2,5,2,2,1,6]
ans=0

for i in range(len(groups)):
    groups[i]=groups[i]%batchSize
# 盡量湊成batch的倍數就可以讓更多人開心
groups_cnt = collections.Counter(groups)
ans+=groups_cnt[0]# 可整除的是固定班底

if batchSize==1:
    print(ans)
elif batchSize==2:
    #奇數組>1組的話會一組開心>一組不開心>一組開心>一組不開心
    ans+=math.ceil(groups_cnt[1]/2)
elif batchSize==3:
    # 2要跟1湊 1湊不夠的往6湊 1湊還夠就1自己湊
    ans+=min(groups_cnt[1],groups_cnt[2])
    ans+=math.ceil((max(groups_cnt[1],groups_cnt[2])-min(groups_cnt[1],groups_cnt[2]))/3)#2比較多或1比較多都是/3
elif batchSize==4:
    # 4的話3要跟1湊 2跟湊
    # ...HOW??
    ans+=min(groups_cnt[3],groups_cnt[1])
    ans+=math.ceil(groups_cnt[2]/2)
    # 剩餘的3或1跟頂多一個2
    

print(ans)
#%% 參考solution
batchSize = 4
groups = [1,3,2,5,2,2,1,6]

batchSize=3
groups=[1,2,3,4,5,6]
ans=0

for i in range(len(groups)):
    groups[i]=groups[i]%batchSize
# 盡量湊成batch的倍數就可以讓更多人開心
print(groups)
groups_cnt = collections.Counter(groups)
print(groups_cnt)
ans+=groups_cnt[0]# 可整除的是固定班底
groups_cnt[0]=0# 歸0

# 接下來處理兩個相加
for i in range(1,batchSize):
    if groups_cnt[i]>0:
        # 如果兩個不相等
        if (batchSize-i)!=i:
            comb = min(groups_cnt[i],groups_cnt[batchSize-i])
            groups_cnt[i]-= comb
            groups_cnt[batchSize-i]-= comb
            ans+=comb
        else:
            comb=(groups_cnt[i])//2
            groups_cnt[i]-=comb*2
            ans+=comb
# 接下來就不會了 針對還剩下的處理
print(ans)
print(groups_cnt)

new_groups = [] # 這裡要把剩下的梅珮到的變回原來groups的樣子
for group, count in groups_cnt.items():
    new_groups += [group] * count

#@lru_cache(None)
def bruteforce(remainder, new_groups):
    if not new_groups:
        return 0
    ans_tp=0 # 增加湊成功的組合
    for i in range(len(new_groups)): # 針對new_groups裡面剩下的每一個去遍歷
        new_groups2=new_groups[:i]+new_groups[i+1:]# 剩下的=全部扣掉現在遍歷的
        remainder2=(remainder-new_groups[i])%batchSize# 加上目前這個之後的餘數
        ans_tp=max(ans_tp,bruteforce(remainder2,new_groups2))#  這裡看不懂!!!ans_tp的部分 後面可以理解是把剩下的又丟進去算
    return ans_tp+int(remainder==0)# 看這次傳進來的有沒有得+1
print(bruteforce(0,tuple(new_groups))+ans)
        
