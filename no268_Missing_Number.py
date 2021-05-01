# My solution
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n_set = set(range(len(nums)+1))
        for i in range(len(nums)):
            n_set.remove(nums[i])
        return list(n_set)[0]
#%% Better way by official solution
class Solution:
def missingNumber(self, nums):
    num_set = set(nums)
    n = len(nums) + 1
    for number in range(n):
        if number not in num_set:
            return number
#%% My solution: sort
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        for i in range(len(nums)):
            if nums[i]!=i:
                return i
        return len(nums)
#%% Official solution 3: XOR
class Solution:
def missingNumber(self, nums):
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= i ^ num
    return missing
#%% Sum solution. Brilliant!!
class Solution:
    def missingNumber(self, nums):
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum