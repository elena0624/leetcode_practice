# TLE brute force解
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums)):
            cur=0
            for j in range(i+1,len(nums)):
                if nums[j]<nums[i]:
                    cur+=1
            ans.append(cur)
        return(ans)
#%% My revised solution
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans=nums.copy()
        sorted_cnt=[]
        for i in range(len(nums)-1,-1,-1):
            pos=bisect.bisect_left(sorted_cnt,nums[i])
            ans[i]=pos
            sorted_cnt.insert(pos,nums[i])
        return(ans)
#%% BIT 
class Solution:
    def countSmaller(self, nums):
    # rank=第幾小的
        rank, N, res = {val: i + 1 for i, val in enumerate(sorted(nums))}, len(nums), []
        BITree = [0] * (N + 1)

        def update(i):# binary indexed tree概念 
            while i <= N:
                BITree[i] += 1
                i += (i & -i)

        def getSum(i):
            s = 0
            while i:
                s += BITree[i]
                i -= (i & -i)
            return s

        for x in reversed(nums):
            res += getSum(rank[x] - 1),
            update(rank[x])
        return res[::-1]
#%% 快解
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # implement Binary Index Tree
        def update (index, value, tree, size):
            index+=1
            while index < size:
                tree[index] += value
                index += index & -index
                
        def query(index, tree):
            res = 0
            while index >= 1:
                res += tree[index]
                index -=  index & -index 
            return res
        
       
        
        offset = 10**4
        size = 2*10**4 +2
        
        tree = [0] * size
        result = []
        for num in reversed(nums):
            smaller_count = query(num+offset, tree)
            result.append(smaller_count)
            update(num+offset, 1, tree, size)
        return reversed(result)