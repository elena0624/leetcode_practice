#%% 1812. Determine Color of a Chessboard Square
class Solution: # My solution
    def squareIsWhite(self, coordinates: str) -> bool:
        le_dic={}
        for i,le in enumerate(list(string.ascii_lowercase[:9])):
            le_dic[le]=i
        if ((le_dic[coordinates[0]])%2+(int(coordinates[1]))%2)==1:
            return(False)
        else:
            return(True)
#%% Others solution
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
    return (ord(coordinates[0]) + ord(coordinates[1])) % 2
#%% 1813. Sentence Similarity III
class Solution: #My solution
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if sentence1==sentence2:
            return(True)

        # 若長的頭=短的頭 長的尾=短的尾就可以
        # 都先切成words
        ls_list = sentence1.split()
        ss_list = sentence2.split()

        if len(ls_list)==len(ss_list) and ls_list!=ss_list:
            return(False)

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
            return(True)
        # 代表~i-1是一樣的
        # 比對尾
        for j in range(len(ss_list)):
            if ls_list[-1-j]==ss_list[-1-j]:
                continue
            else:
                break
        # 後半段完全一樣
        if ls_list[-1-j:]==ss_list:
            return(True)

        # 代表-j+1到最後一個是一樣的
        # 若完全步一樣就是0 完全一樣就是?
        print(i+j)

        if (i+j)==len(ss_list):
            return(True)
        else:
            return(False)
#%% Other solutions 1
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s = sentence1.split(" ")
        t = sentence2.split(" ")
        n, m = len(s), len(t)
        if n > m:
            s, t = t, s
            n, m = m, n
        pre = 0
        while pre < n and s[pre] == t[pre]:
            pre += 1
        suf = 0
        while suf < n and s[-1 - suf] == t[-1 - suf]:
            suf += 1
        return pre + suf >= n
#%% Other solutions 2
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        s1 = sentence1.split()
        s2 = sentence2.split()
        if(len(s1)>len(s2)):            #let s1 be the smaller and s2 be the greater
            s1,s2 = s2,s1
        while(s1): 
            if(s2[0]==s1[0]):
                s2.pop(0)
                s1.pop(0)
            elif(s2[-1]==s1[-1]):
                s2.pop()
                s1.pop()
            else:
                return(False)            
        return(True)
#%% 1814. Count Nice Pairs in an Array
class Solution: # My solution
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10**9+7
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

        return(ans%mod)
#%% Other Solutions
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        freqs = Counter(num - int(str(num)[::-1]) for num in nums)
        return sum(freq * (freq - 1) // 2 for freq in freqs.values()) % 1000000007
# %% 1815. Maximum Number of Groups Getting Fresh Donuts
class Solution: # Solution according to others. WILL TLE IF DIDN'T USE @lru_cache(None) !!!!
    def maxHappyGroups(self, B, groups):
        ans=0

        for i in range(len(groups)):
            groups[i]=groups[i]%B
        # 盡量湊成batch的倍數就可以讓更多人開心
        groups_cnt = collections.Counter(groups)
        ans+=groups_cnt[0]# 可整除的是固定班底
        groups_cnt[0]=0# 歸0
        
        # 接下來處理兩個相加
        for i in range(1,B):
            if groups_cnt[i]>0:
                # 如果兩個不相等
                if (B-i)!=i:
                    comb = min(groups_cnt[i],groups_cnt[B-i])
                    groups_cnt[i]-= comb
                    groups_cnt[B-i]-= comb
                    ans+=comb
                else:
                    comb=(groups_cnt[i])//2
                    groups_cnt[i]-=comb*2
                    ans+=comb

        new_groups = [] # 這裡要把剩下的梅珮到的變回原來groups的樣子
        for group, count in groups_cnt.items():
            new_groups += [group] * count

        @lru_cache(None)# important
        def bruteforce(remainder, new_groups):
            if not new_groups:
                return 0
            ans_tp=0 # 增加湊成功的組合
            for i in range(len(new_groups)): # 針對new_groups裡面剩下的每一個去遍歷
                new_groups2=new_groups[:i]+new_groups[i+1:]# 剩下的=全部扣掉現在遍歷的
                remainder2=(remainder-new_groups[i])%B# 加上目前這個之後的餘數
                ans_tp=max(ans_tp,bruteforce(remainder2,new_groups2))#  這裡看不懂!!!ans_tp的部分 後面可以理解是把剩下的又丟進去算
            return ans_tp+int(remainder==0)# 看這次傳進來的有沒有得+1
        return(bruteforce(0,tuple(new_groups))+ans)
#%% Other solution1
class Solution:
    def maxHappyGroups(self, B, groups):
        ans = sum(g%B == 0 for g in groups)
        groups = [g for g in groups if g%B != 0]

        pos = [0]*B
        for g in groups: pos[g%B] += 1

        for i in range(1, B):
            t = min(pos[i], pos[B-i]) if 2*i != B else pos[i]//2
            ans += t
            pos[i] -= t
            pos[B-i] -= t
            
        if sum(pos) == 0: return ans

        @lru_cache(None)
        def dfs(position, last):
            if sum(position) == 0: return 0

            ans = float("-inf")
            for i in range(B):
                if position[i] > 0:
                    t = [j for j in position]
                    t[i] -= 1
                    U = (last - i) % B
                    ans = max(ans, dfs(tuple(t), U) + (U == 0))
                      
            return ans

        return max(dfs(tuple(pos), i) for i in range(1, B)) + ans
#%% Other solution2
from collections import defaultdict
class Solution:
    def maxHappyGroups(self, batchsize: int, groups: List[int]) -> int:
        n = len(groups)
        group = [g%batchsize for g in groups if g%batchsize!=0]
        satisfied = n-len(group)
        matching = defaultdict(int)
        for g in group:
            if matching[batchsize-g]>0:
                matching[batchsize-g]-=1
                satisfied+=1
            else:
                matching[g]+=1
        groups = []
        for group,count in matching.items():
            groups+=[group]*count
        @lru_cache(None)
        def helper(leftover,groups):
            if not groups:
                return 0
            result = 0
            for i in range(len(groups)):
                nextgroup = groups[:i]+groups[i+1:]
                nextleftover = (leftover-groups[i])%batchsize
                result = max(result,helper(nextleftover,nextgroup))
            return result+int(leftover==0)
        return helper(0,tuple(groups))+satisfied