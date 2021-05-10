#%% My solution
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        n=len(target)
        
        if n==1:
            return target[0]==1
        
        target = [-1*a for a in target]
        heapq.heapify(target)

        while target[0]<-1:
            cur_large = heapq.heappop(target)
            other_sum = sum(target)
            sec_large = target[0]
            
            if sec_large==-1:
                if (cur_large+1)%other_sum==0:
                    return(True)
                else:
                    return(False)
            prev_large = cur_large-(((cur_large-sec_large)//other_sum)+1) * other_sum
            if prev_large>-1:
                return(False)
            heapq.heappush(target,prev_large)
        #if target.count(-1)==n:
        #    return(True)
        #else:
        #    return(False)
#%%
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = [-num for num in target]
        total = sum(target)
        heapify(heap)
        while heap[0] != -1:
            num = -heappop(heap)
            total -= num
            if num <= total or total < 1: return False
            num %= total
            total += num
            heappush(heap, -num or -total)
        return True