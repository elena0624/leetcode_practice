class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        acc_nums = [0]+nums.copy()
        max_ans=0
        last_idx=1
        for i in range(2,len(nums)+1):
            acc_nums[i] += acc_nums[i-1]

        l=r=0
        seen=dict()
        while r<len(nums):
            if seen.get(nums[r],-1)>=0:
                l=max(seen[nums[r]]+1,l)
                seen[nums[r]] = r
            else:# 沒看過
                seen[nums[r]]=r
            #print('r',r,'l',l,'目前subarray',acc_nums[r+1]-acc_nums[l])
            max_ans=max(max_ans,acc_nums[r+1]-acc_nums[l])
            r+=1
        return(max_ans)
#%% Faster
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        last = replySum = currSum = 0
        cache = set()
        for i in range(len(nums)):
            if nums[i] in cache:# 如果已存在
                replySum = max(replySum, currSum)# 目前的結果拿出來比較
                while nums[last] != nums[i]:# 把前面的一一移掉 但重復的個不清 因為-重複的那個+現在的這個=都不要動作
                    currSum -= nums[last]
                    cache.remove(nums[last])
                    last += 1
                last += 1# 移完了 移到上一次出現的
            else:
                cache.add(nums[i]) # 不存在
                currSum += nums[i] # 加下去
        return max(replySum, currSum)
#%% Revised for my code but not Faster
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        acc_nums = [0]+nums.copy()
        max_ans=0
        last_idx=1
        for i in range(2,len(nums)+1):
            acc_nums[i] += acc_nums[i-1]

        l=r=0
        seen=dict()
        while r<len(nums):
            if seen.get(nums[r],-1)>=0:
                max_ans=max(max_ans,acc_nums[r]-acc_nums[l])
                l=max(seen[nums[r]]+1,l)
                seen[nums[r]] = r
            else:# 沒看過
                seen[nums[r]]=r
            r+=1
        return(max(max_ans,acc_nums[r]-acc_nums[l]))