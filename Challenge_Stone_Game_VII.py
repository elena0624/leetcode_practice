# TLE=> bad first try
from functools import lru_cache
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        @lru_cache(maxsize=)
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
        return(get_result(tuple(stones), True))
#%% Bad attemp2 TLE
from functools import lru_cache
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        dp=dict()
        parity=len(stones)%2

        l=0
        stone_len=len(stones)

        #奇數的話是alice拿最後一個 沒分
        #偶數的話是bob拿最後一個 有分
        @lru_cache(maxsize=100000000)
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
        return(get_result(l,stone_len))
#%% Accepted answer=> can be improved
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n=len(stones)
        dp=[[None for i in range(n+1)] for j in range(n+1)]
        parity=len(stones)%2

        for i in range(1,n+1):#長度
            for l in range(n-i+1):#起點
                if i==1:
                    dp[1][l]=stones[l] if parity==0 else 0
                else:
                    if i%2+parity!=1:#alice拿
                        dp[i][l]=max(dp[i-1][l],dp[i-1][l+1])
                    else:# bob拿
                        dp[i][l]=min(dp[i-1][l]+stones[l+i-1],dp[i-1][l+1]+stones[l])
        return(dp[n][0])
#%% Cleaner solution, but space O(n^2)
class Solution:
    def stoneGameVII(self, s: List[int]) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        p_sum = [0] + list(accumulate(s))
        for i in range(len(s) - 2, -1, -1):
            for j in range(i + 1, len(s)):
                dp[i][j] = max(p_sum[j + 1] - p_sum[i + 1] - dp[i + 1][j], 
                               p_sum[j] - p_sum[i] - dp[i][j - 1]);
        return dp[0][len(s) - 1]
#%% space O(n) solution
class Solution:
    def stoneGameVII(self, S: List[int]) -> int:
        N = len(S)
        dpCurr, dpLast = [0] * N, [0] * N
        for i in range(N - 2, -1, -1):# i存左邊
            total = S[i]# 計算目前的總和 從起點i開始
            dpLast, dpCurr = dpCurr, dpLast# 
            for j in range(i + 1, N):# j存右邊，從剩下兩個開始(j=i+1)
                total += S[j]# 把右邊的加進去
                dpCurr[j] = max(total - S[i] - dpLast[j], total - S[j] - dpCurr[j-1])# 要計算ａｂ間的差，這次拿頭後的得分是total-S[i]，要扣掉少去頭的分數；這次拿尾的得分是total-S[j]，一樣要扣掉少尾的分數
        return dpCurr[-1]
#%% My recommend Solution
class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        n = len(stones)
        dp = [0] * n

        for i in range(n - 1, -1, -1):# 一樣起點
            v = stones[i]# 起點值
            run_sum = 0# sum

            for j in range(i + 1, n):# 一樣終點
                new_run = run_sum+stones[j]#不算起點的sum
                dp[j] = max(new_run - dp[j], run_sum+v - dp[j - 1])#拿頭=不算起點的sum-前一輪的解;拿尾=不算起點也不算終點的sum+起點-前一輪-1的結果
                run_sum = new_run#此輪不算起點的sum 
        return dp[n - 1]