class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        last_dic={}
        for i in range(len(nums)):
            if nums[i] in last_dic:
                return(last_dic[nums[i]],i)
            else:
                last_dic[target-nums[i]]=i
