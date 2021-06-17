# My solution
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        cur=0
        ans=0
        low=0
        cur_max=False
        for i in range(len(nums)):
            # 直接爆開
            if nums[i]>right:
                cur=0
                cur_max=False
            # 符合標準
            elif nums[i]>=left and nums[i]<=right:
                # 連續的
                low=0
                ans+=1
                ans+=cur
                cur+=1
                cur_max=True
            # 不符標準，但前面有cur_max可以靠
            elif nums[i]<left:
                if cur_max:
                    ans+=cur
                    ans-=low
                cur+=1
                low+=1
           # print('ans',ans,'cur',cur,'curmax',cur_max)
        return(ans)
#%% other
class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        ans = 0
        prev = -1
        dp = 0
        # print(M)
        for i in range(len(A)):
            if A[i] < L:
                ans += dp
            elif A[i] > R:
                dp = 0
                prev = i
            else:
                dp = i - prev
                ans += dp
        return ans
#%% other 
class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        ans, low, mid = 0, 0, 0
        for num in nums:
            if num > right: mid = 0
            else:
                mid += 1
                ans += mid
            if num >= left: low = 0
            else:
                low += 1
                ans -= low
        return ans
#%% elegant!!
class Solution:
    def numSubarrayBoundedMax(self, A, L, R):
        L_ind, R_ind, ans = -1, -1, 0
        for i, num in enumerate(A):
            if num >= L: L_ind = i
            if num > R:  R_ind = i
            ans += L_ind - R_ind
        return ans
