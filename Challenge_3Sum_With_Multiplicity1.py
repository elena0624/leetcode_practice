# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 01:48:48 2021

@author: ppj
"""

# 3sum with multiplicity
#arr = [1,1,2,2,3,3,4,4,5,5]
#target = 8

arr = [1,1,2,2,2,2]
target = 5

# 最簡單暴力=>三個回圈開下去
# 省一點時間=>把大問題拆解成小問題=>扣掉第一個數後就變成2sum問題=>就可參照2sum的作法=>感覺就是3sum=>拆成一個2sum
sol = 0 # 初始解的數量
for i in range(len(arr)-2):# 可少一個因為一定要留兩個
    value_counts = {} # 這裡的dictionary存次數!
    target_2 = target-arr[i]
    arr_2 = arr[i+1:]
    # 這裡先來創一個value counts的dictionary# 
    value_counts = {x:arr_2.count(x) for x in arr_2}
    print(value_counts)
    print([*value_counts])
    sorted_keys = sorted([*value_counts])
#    print(len(value_counts))
    # 按照key的大小來看
    for j in range(len(value_counts)):
        key = sorted_keys[j]
        left_value = target_2-key
        if key>left_value:
            break
        elif (key<left_value) and (left_value in sorted_keys):
            print('key:',key)
            print('leftvalue:',left_value)
        
            sol += value_counts[left_value]*value_counts[key]
        elif key==left_value:
            print('key:',key)
            print('leftvalue:',left_value)

            sol += value_counts[key]*(value_counts[key]-1)/2
        print(sol)
    print(sol)
print(int(sol))


#%%結果數太大了 看了一下怎麼樣去處理=> Time Limit Exceed
M = 10**9 + 7 # 取MOD處理

arr = [1,1,2,2,3,3,4,4,5,5]
target = 8
#arr = [1,1,2,2,2,2]
#target = 5

# 最簡單暴力=>三個回圈開下去
# 省一點時間=>把大問題拆解成小問題=>扣掉第一個數後就變成2sum問題=>就可參照2sum的作法=>感覺就是3sum=>拆成一個2sum
sol = 0 # 初始解的數量
for i in range(len(arr)-2):# 可少一個因為一定要留兩個
    value_counts = {} # 這裡的dictionary存次數!
    target_2 = target-arr[i]
    arr_2 = arr[i+1:]
    # 這裡先來創一個value counts的dictionary# 
    value_counts = {x:arr_2.count(x) for x in arr_2}
    print(value_counts)
    print([*value_counts])
    sorted_keys = sorted([*value_counts])
#    print(len(value_counts))
    # 按照key的大小來看
    for j in range(len(value_counts)):
        key = sorted_keys[j]
        left_value = target_2-key
        if key>left_value:
            break
        elif (key<left_value) and (left_value in sorted_keys):
            print('key:',key)
            print('leftvalue:',left_value)
        
            sol += (value_counts[left_value]*value_counts[key])%M # 取MOD處理
        elif key==left_value:
            print('key:',key)
            print('leftvalue:',left_value)

            sol += (value_counts[key]*(value_counts[key]-1)/2)%M # 取MOD處理
        print(sol)
    print(sol)
print(int(sol%M))
#%%
#arr = [1,1,2,2,3,3,4,4,5,5]
#target = 8
#arr = [1,1,2,2,2,2]
#target = 5
arr = [3,3,0,0,3,2,2,3]
target = 6


# 最簡單暴力=>三個回圈開下去
# 省一點時間=>把大問題拆解成小問題=>扣掉第一個數後就變成2sum問題=>就可參照2sum的作法=>感覺就是3sum=>拆成一個2sum
M = 10**9 + 7 # 取MOD處理
sol = 0 # 初始解的數量
# 直接全部排序來做value counts
value_counts = {x:arr.count(x) for x in arr}
sorted_keys = sorted([*value_counts])
print('v_c',value_counts)
print('sorted_keys',sorted_keys)
for i in range(len(value_counts)):
    key = sorted_keys[i]
    left_value = target-key
    print('key',key)
    print('left_value',left_value)
    print('sol',sol)
    if key*3>target: # 後面兩個數至少跟自己一樣大
        continue        
    else:
        if key*3==target:# =三個數加起來 3key=target的情況
            if value_counts[key]>=3:
                sol += ((value_counts[key])*(value_counts[key]-1)*(value_counts[key]-2)/6%M)# Cn取3
            continue # 後面就不能繼續算了!!
        if (target-key*2) in sorted_keys:#2key+n=target的情況 # 不能用else 後續可能還有解
            sol += ((value_counts[key])*(value_counts[key]-1)/2%M)*value_counts[target-key*2]%M# Cn取2*n的數量
#        if : # key*3<left_value:回到下面的解
        for j in range(i+1,len(value_counts)):#  剩下的組合
            key2 = sorted_keys[j]
            left_value2 = target-key-key2
            print('key2',key2)
            print('left_value2',left_value2)
            if key2>left_value2:
                continue
            elif (key2<left_value2) and (left_value2 in sorted_keys):
                sol += (value_counts[left_value2]*value_counts[key2])%M*value_counts[key] # 再*自己的數量 取MOD處理
            elif key2==left_value2:
                sol += (value_counts[key2]*(value_counts[key2]-1)/2)%M*value_counts[key] # 再*自己的數量 取MOD處理
print(int(sol%M))
#%% 
A=[3,3,0,0,3,2,2,3]
target = 6

MOD = 10**9 + 7
count = [0] * 101 # 因為題目有寫 0 <= arr[i] <= 100 所以他直接建一個array來儲存0~100出現的次數
for x in A:
    count[x] += 1 #=我的value counts

ans = 0

# All different
for x in range(101):
    for y in range(x+1, 101):
        z = target - x - y
        if y < z <= 100:
            ans += count[x] * count[y] * count[z]
            ans %= MOD

# x == y
for x in range(101):
    z = target - 2*x
    if x < z <= 100:
        ans += count[x] * (count[x] - 1) / 2 * count[z]
        ans %= MOD

# y == z
for x in range(101):
    if (target - x) % 2 == 0:
        y = (target - x) / 2
        if x < y <= 100:
            ans += count[x] * count[int(y)] * (count[int(y)] - 1) / 2
            ans %= MOD

# x == y == z
if target % 3 == 0:
    x = target / 3
    if 0 <= x <= 100:
        ans += count[int(x)] * (count[int(x)] - 1) * (count[int(x)] - 2) / 6
        ans %= MOD

print(int(ans))
