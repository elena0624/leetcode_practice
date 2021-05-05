# My solution
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        unreach=list(range(n-1))
        steps=0
        pre_steps=[n-1]
        while unreach:
            steps+=1
            cur_steps=[]
            for j in pre_steps:
                if j<=nums[0]:
                    return(steps)
                for i in unreach:
                    if (j-i)<=nums[i]:
                        unreach.remove(i)
                        cur_steps.append(i)
            pre_steps=cur_steps

        return(steps)
#%% Other solution
class Solution:
    def jump(self, nums):
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return times
#%% O(n) solution
class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        # destination is last index
        destination = size - 1
        # record of current coverage, record of last jump index
        cur_coverage, last_jump_index = 0, 0
        # counter for jump
        times_of_jump = 0
         # Quick response if start index == destination index == 0
        if size == 1:
            return 0
        # Greedy strategy: extend coverage as long as possible with lazy jump
        for i in range( 0, size):
            # extend current coverage as further as possible
            cur_coverage = max( cur_coverage, i + nums[i] ) # 從現在這步加上去能不能走得更遠=> 目前走最遠的
            # forced to jump (by lazy jump) to extend coverage  
            if i == last_jump_index: # 如果現在這裡=上次走最遠的地方
                # update last jump index
                last_jump_index = cur_coverage # 把上次走最遠的地方更新成目前走最遠的地方
                # update counter of jump by +1
                times_of_jump += 1
                # check if reached destination already
                if cur_coverage >= destination:
                        return times_of_jump
        return times_of_jump
#%% Elegant solution
class Solution:
    def jump(self, n: List[int]) -> int:
        currEnd = currFarthest = jump = 0
        l = len(n)
        for i in range(l-1):
            currFarthest = max(currFarthest, i + n[i])
            if i == currEnd:
                jump+=1
                currEnd = currFarthest
            
        return jump

