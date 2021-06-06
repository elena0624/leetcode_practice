#%% My answer
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_ans=0
        un_seen=set(nums)
        for i in range(len(nums)):
            cur_l=0
            if nums[i] in un_seen:
                un_seen.remove(nums[i])
                cur_l=1
                l=r=nums[i]
                while l-1 in un_seen:
                    l-=1
                    un_seen.remove(l)
                    cur_l+=1
                while r+1 in un_seen:
                    r+=1
                    un_seen.remove(r)
                    cur_l+=1
                max_ans = max(cur_l,max_ans)
        return(max_ans)
#%% More elegant answer
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = set(nums)
        longest = 0
        
        for num in nums:
            if num - 1 in nums:            
                continue

            current = 1
            seq_num = num
            
            while seq_num + 1 in nums:
                current += 1
                seq_num += 1

            longest = max(longest, current)
        
        return longest
