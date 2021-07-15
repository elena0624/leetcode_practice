#%% My solution(O(N^2logn))
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        ans=0
        nums = sorted(nums)

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                idx = bisect.bisect_left(nums,nums[i]+nums[j])
        #        print('i',i,'j',j,'idx',idx)
        #        print(max(0,idx-1-j))
                ans+=max(0,idx-1-j)
        return(ans)
#%% Elegant solution(O(n^2))
class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        c = 0
        n = len(nums)
        nums.sort()
        for i in range(n-1,1,-1):
            lo = 0
            hi = i - 1
            while lo < hi:
                if nums[hi]+nums[lo] > nums[i]:
                    c += hi-lo
                    hi -= 1
                else:
                    lo += 1
        return c