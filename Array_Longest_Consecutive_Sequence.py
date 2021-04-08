class Solution: # My solution
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        i=0
        lg_ans=0
        while i<len(nums):
            ans=1
            r=i
            while r<(len(nums)-1) and ((nums[r]+1)==nums[r+1]):
        #        print((nums[r]+1))
        #        print(nums[r+1])

                r+=1
                ans+=1
            lg_ans = max(lg_ans, ans)
            i=r+1
        return(lg_ans)
#%% official Solution= Sorted
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak
#%% official Solution= Hastset
class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak