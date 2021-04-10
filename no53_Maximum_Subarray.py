class Solution: #My solution
    def maxSubArray(self, nums: List[int]) -> int:
        #O(n)作法
        lc_sum=-10**6
        left=0
        for i in range(len(nums)):
            # 比較在前n者的情況下是否要包含
            if left>0:
                #要包含左邊 那看看左邊有無比較大
                if nums[i]<0:
                    lc_sum = left if left>lc_sum else lc_sum
                else:
                    lc_sum = left+ nums[i] if (left+ nums[i])>lc_sum else lc_sum
                # 要包含左邊 更新左邊數字
                left = left + nums[i] 

            else:
                left = nums[i]
                # 步包含左邊 納比自己有沒有比目前最大值大
                lc_sum = nums[i] if nums[i]>lc_sum else lc_sum

        return(lc_sum)
#%% Revised solution
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #O(n)作法
        lc_sum=-10**6
        left=0

        for i in range(len(nums)):
            left+=nums[i]
            lc_sum = max(left,lc_sum)
            left = max(left,0)
        return(lc_sum)
#%% Divide and conquer solution1
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def findBestSubarray(nums, left, right):
            # Base case - empty array.
            if left > right:
                return -math.inf

            mid = (left + right) // 2
            curr = best_left_sum = best_right_sum = 0

            # Iterate from the middle to the beginning.
            for i in range(mid - 1, left - 1, -1):
                curr += nums[i]
                best_left_sum = max(best_left_sum, curr)

            # Reset curr and iterate from the middle to the end.
            curr = 0
            for i in range(mid + 1, right + 1):
                curr += nums[i]
                best_right_sum = max(best_right_sum, curr)

            # The best_combined_sum uses the middle element and
            # the best possible sum from each half.
            best_combined_sum = nums[mid] + best_left_sum + best_right_sum

            # Find the best subarray possible from both halves.
            left_half = findBestSubarray(nums, left, mid - 1)
            right_half = findBestSubarray(nums, mid + 1, right)

            # The largest of the 3 is the answer for any given input array.
            return max(best_combined_sum, left_half, right_half)
        
        # Our helper function is designed to solve this problem for
        # any array - so just call it using the entire input!
        return findBestSubarray(nums, 0, len(nums) - 1)
#%% divide and conquer solution2
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def divide_and_conquer(nums, i, j):
            if i == j-1:
                return nums[i],nums[i],nums[i],nums[i]
            
            # we will compute :
            # a which is max contiguous sum in nums[i:j] including the first value
            # m which is max contiguous sum in nums[i:j] anywhere 
            # b which is max contiguous sum in nums[i:j] including the last value
            # s which is the sum of all values in nums[i:j]
                
            # compute middle index to divide array in two halves
            i_mid = i+(j-i)//2
            
            # compute a, m, b, s for left half
            a1, m1, b1, s1 = divide_and_conquer(nums, i, i_mid)
            
            # compute a, m, b, s for right half
            a2, m2, b2, s2 = divide_and_conquer(nums, i_mid, j)
            
            # combine a, m, b, s values from left and right halves to form a, m, b, s for whole array (bottom up)
            a = max(a1, s1+a2)
            b = max(b2, s2+b1)
            m = max(m1,m2,b1+a2)
            s = s1+s2
            return a,m,b,s
                  
        _,m,_,_ = divide_and_conquer(nums, 0, len(nums))
