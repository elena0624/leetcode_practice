#%% My O(n) solution
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if len(nums)==1:
                return 0
            elif i==0:
                if nums[i]>nums[i+1]:
                    return i
            elif i==len(nums)-1:
                if nums[i]>nums[i-1]:
                    return i
            elif nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i

#%% Elegant O(n) solution
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return i
        return len(nums)-1

#%% O(logn) solution
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<r:
            #print(l,r)
            mid = (l+r)//2
            if nums[mid]>nums[mid+1]:
                r=mid
            else:
                l=mid+1
        return(l)