class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        mean=sorted(nums)[len(nums)//2]
        return(sum(abs(num-mean) for num in nums))
