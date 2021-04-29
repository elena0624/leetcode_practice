# My solution (ugly)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        l=0
        r=n-1
        mid = (l+r)//2
        f_ans=-1
        if not nums:
            return([-1,-1])

        while mid!=l and mid!=r:
            if target<nums[mid]:
                r=mid
            elif target==nums[mid]:
                f_ans=mid
                break
            else:
                l=mid
            mid=(l+r)//2
        if target==nums[mid]:
            f_ans=mid
        elif target==nums[r]:
            f_ans=r
        elif target==nums[l]:
            f_ans=l
        if f_ans==-1:
            return([-1,-1])
        else:
            # 從前後找
            s_ans=f_ans
            l_ans=f_ans
            while (s_ans>0 and nums[s_ans-1]==target) or (l_ans<n-1 and nums[l_ans+1]==target):
                if s_ans>0 and nums[s_ans-1]==target:
                    s_ans-=1
                if l_ans<n-1 and nums[l_ans+1]==target:
                    l_ans+=1
        return([s_ans,l_ans])
#%% Other's code
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Key idea here is we are modifying binary search to find the first / last target elements respectiveely
        # when finding the first value 
        # when we find our value, we take a look at whether the middle element is the first element in the array. if so, return the index
        # if its not the first element in the array, check the element before.
        # if the element before is equal to the current element, discard the second half of the array and search the first half
        # if the elment before is not equal to the current element, save the middle index
        # do the reverse to find the last element
        result = [-1, -1]
        left = 0
        right = len(nums)-1
        
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                if pivot == 0 or (pivot > 0 and nums[pivot-1] != target):
                    result[0] = pivot
                    break
                else:
                    right = pivot - 1
            elif nums[pivot] > target:
                right = pivot - 1
            else:
                left = pivot + 1
                
        if result[0] == -1:
            return result
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] == target:
                if pivot == len(nums)-1 or (pivot < len(nums)-1 and nums[pivot+1] != target):
                    result[1] = pivot
                    break
                else:
                    left = pivot + 1
            elif nums[pivot] > target:
                right = pivot - 1
            else:
                left = pivot + 1
        
        return result