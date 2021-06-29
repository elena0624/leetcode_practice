#%% TLE answer. Not sure if correct
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        for i in range(len(nums),0,-1):
            z_cnt=i-sum(nums[:i])
            if z_cnt<=k:
                return i
            for j in range(1,len(nums)-i+1):
                z_cnt-=(nums[j-1]==0)# 頭要不要扣
                z_cnt+=(nums[j+i-1]==0)# 尾要不要扣
                if z_cnt<=k:
                    return i
        return 0
#%% 
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        z_cnt=0
        left=0 # 起點
        ans=0
        for i in range(len(nums)):# 檢查每一個是不是0
            if nums[i]==0:
                z_cnt+=1
        #    print(z_cnt)
            while z_cnt>k: #若目前要改的已經超過 要把起始點移到不會超過的地方(最慘就是直接移到i的右邊)
                if nums[left]==0:
                    z_cnt-=1
                left+=1
            ans=max(ans,i-left+1)   
        return(ans)
#%% Recommend answer! fast and elegant
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = 0
        for j in range(len(nums)):
            k -= 1 - nums[j]
            if k < 0:
                k += 1 - nums[i]
                i += 1
        return(j - i + 1)