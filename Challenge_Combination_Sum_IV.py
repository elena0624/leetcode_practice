# Brute force method=>TLE
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.cnt=0
        def dfs_search(cur):
            if cur==target:
                self.cnt+=1
                return
            elif cur>target:
                return
            else:
                for i in nums:
                    dfs_search(cur+i)
            return

        dfs_search(0)
        return(self.cnt)
#%% Climbing stairs
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp=collections.defaultdict(int)
        for i in nums:
            dp[i]+=1
            
        for i in range(target+1):
            temp=0
            temp+=dp[i]
            for j in nums:
                temp+=dp[i-j]
            dp[i]=temp
        return(temp)
#%% Revised
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp=collections.defaultdict(int)
        dp[0]=1

        for i in range(target+1):
            temp=0
            temp+=dp[i]
            for j in nums:
                temp+=dp[i-j]
            dp[i]=temp
        return(temp)




