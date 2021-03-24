class Solution1: #wrong answer,TLE
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        sol = 0 # 初始解的數量
        M = 10**9 + 7 # 取MOD處理
        for i in range(len(arr)-2):# 可少一個因為一定要留兩個
            value_counts = {} # 這裡的dictionary存次數!
            target_2 = target-arr[i]
            arr_2 = arr[i+1:]
            # 這裡先來創一個value counts的dictionary# 
            value_counts = {x:arr_2.count(x) for x in arr_2}
            sorted_keys = sorted([*value_counts])
            # 按照key的大小來看
            for j in range(len(value_counts)):
                key = sorted_keys[j]
                left_value = target_2-key
                if key>left_value:
                    break
                elif (key<left_value) and (left_value in sorted_keys):
                    sol += (value_counts[left_value]*value_counts[key])%M
                elif key==left_value:
                    sol += (value_counts[key]*(value_counts[key]-1)/2)%M
        return(int(sol%M))
#%%
class Solution2: #accepted but slow
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        M = 10**9 + 7 # 取MOD處理
        sol = 0 # 初始解的數量
        # 直接全部排序來做value counts
        value_counts = {x:arr.count(x) for x in arr}
        sorted_keys = sorted([*value_counts])
        for i in range(len(value_counts)):
            key = sorted_keys[i]
            #print('key',key)
            #print('sol',sol)
            if key*3>target: # 後面兩個數至少跟自己一樣大
                continue        
            else:
                if key*3==target:# =三個數加起來 3key=target的情況
                    if value_counts[key]>=3:
                        sol += ((value_counts[key])*(value_counts[key]-1)*(value_counts[key]-2)/6)# Cn取3
                    continue
                if (target-key*2) in sorted_keys:#2key+n=target的情況 # 不能用else 後續可能還有解
                    sol += ((value_counts[key])*(value_counts[key]-1)/2)*value_counts[target-key*2]# Cn取2*n的數量
        #        if : # key*3<left_value:回到下面的解
                for j in range(i+1,len(value_counts)):#  剩下的組合
                    key2 = sorted_keys[j]
                    left_value2 = target-key-key2
                    if key2>left_value2:
                        continue
                    elif (key2<left_value2) and (left_value2 in sorted_keys):
                        sol += (value_counts[left_value2]*value_counts[key2])*value_counts[key] # 再*自己的數量 取MOD處理
                    elif key2==left_value2:
                        sol += (value_counts[key2]*(value_counts[key2]-1)/2)*value_counts[key] # 再*自己的數量 取MOD處理
        return(int(sol%M))
#%% leetcode solution(approach 2)
class Solution3(object):
    def threeSumMulti(self, A, target):
        MOD = 10**9 + 7
        count = [0] * 101
        for x in A:
            count[x] += 1

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

        return int(ans)
#%% More elegant solution (approach3)
class Solution(object):
    def threeSumMulti(self, A, target):
        MOD = 10**9 + 7
        count = collections.Counter(A)
        keys = sorted(count)

        ans = 0

        # Now, let's do a 3sum on "keys", for i <= j <= k.
        # We will use count to add the correct contribution to ans.
        for i, x in enumerate(keys):
            T = target - x
            j, k = i, len(keys) - 1
            while j <= k:
                y, z = keys[j], keys[k]
                if y + z < T:
                    j += 1
                elif y + z > T:
                    k -= 1
                else: # x+y+z == T, now calculate the size of the contribution
                    if i < j < k:
                        ans += count[x] * count[y] * count[z]
                    elif i == j < k:
                        ans += count[x] * (count[x] - 1) / 2 * count[z]
                    elif i < j == k:
                        ans += count[x] * count[y] * (count[y] - 1) / 2
                    else:  # i == j == k
                        ans += count[x] * (count[x] - 1) * (count[x] - 2) / 6

                    j += 1
                    k -= 1

        return int(ans) % MOD
#%% My solution revised
class Solution4:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        M = 10**9 + 7 # 取MOD處理
        sol = 0 # 初始解的數量
        # 直接全部排序來做value counts
        # value_counts = {x:arr.count(x) for x in arr}
        value_counts = collections.Counter(arr)
        # sorted_keys = sorted([*value_counts])
        sorted_keys = sorted(value_counts)
        for i in range(len(value_counts)):
            key = sorted_keys[i]
            #print('key',key)
            #print('sol',sol)
            if key*3>target: # 後面兩個數至少跟自己一樣大
                continue        
            else:
                if key*3==target:# =三個數加起來 3key=target的情況
                   # if value_counts[key]>=3:# 不用這條判斷 因為就算=0.1.2.下面的算是也會=0 不過有沒有這條速度差不多
                    sol += ((value_counts[key])*(value_counts[key]-1)*(value_counts[key]-2)/6%M)# Cn取3
                    continue
                if (target-key*2) in sorted_keys:#2key+n=target的情況 # 不能用else 後續可能還有解
                    sol += ((value_counts[key])*(value_counts[key]-1)/2%M)*value_counts[target-key*2]%M# Cn取2*n的數量
        #        if : # key*3<left_value:回到下面的解
                for j in range(i+1,len(value_counts)):#  剩下的組合
                    key2 = sorted_keys[j]
                    left_value2 = target-key-key2
                    if key2>left_value2:
                        continue
                    elif (key2<left_value2) and (left_value2 in sorted_keys):
                        sol += (value_counts[left_value2]*value_counts[key2])%M*value_counts[key] # 再*自己的數量 取MOD處理
                    elif key2==left_value2:
                        sol += (value_counts[key2]*(value_counts[key2]-1)/2)%M*value_counts[key] # 再*自己的數量 取MOD處理
        return(int(sol%M))