#%% TLE answer. Can ignore these2
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod=10**9+7
        speed = [x for _,x in sorted(zip(efficiency,speed))]
        efficiency = sorted(efficiency)

        max_ans=0
        for i in range(n):
            cur_eff = efficiency[i]
            cur_speed = speed[i] + sum(sorted(speed[i+1:],reverse=True)[:min(k-1,len(speed[i+1:]))])    
            #print(cur_eff,cur_speed)
            max_ans=max(max_ans,cur_eff*cur_speed)
        return(max_ans%mod)
#%% TLE answer2. Can ignore
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod=10**9+7
        speed2 = sorted(zip(speed,efficiency),reverse=True)
        efficiency = sorted(efficiency)
        max_ans=0
        for i in range(n):
            cur_eff = efficiency[i]
            temp_idx=0
            j=0
            cur_speed=0
            while j<n and temp_idx<k:
                if speed2[j][1]>=cur_eff:
                    cur_speed+=speed2[j][0]
                    temp_idx+=1
                j+=1
        #    print(cur_eff,cur_speed)
            max_ans=max(max_ans,cur_eff*cur_speed)
        return(max_ans%mod)
#%% Revised answer
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        mod=10**9+7
        speed = [x for _,x in sorted(zip(efficiency,speed), reverse=True)]
        efficiency = sorted(efficiency, reverse=True)

        heap_speed = []
        sum_speed = 0
        max_ans=0
        for i in range(n):
            if len(heap_speed)<k:
                heapq.heappush(heap_speed,speed[i])
                sum_speed+=speed[i]
            else:
                sum_speed+=speed[i]
                sum_speed-= heapq.heappushpop(heap_speed, speed[i])
            max_ans=max(max_ans,efficiency[i]*sum_speed)
        return(max_ans%mod)
#%% More elegant answer
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        engineers = list(zip(efficiency, speed))
        engineers.sort(reverse=True)  # Sort by decreasing order of efficiency
        minHeap = []
        speedSum = 0
        ans = 0
        for e, s in engineers:
            speedSum += s
            heappush(minHeap, s)
            if len(minHeap) > k:  # Over k engineers -> remove the lowest speed engineer
                speedSum -= heappop(minHeap)
            ans = max(ans, speedSum * e)
        return ans % 1_000_000_007