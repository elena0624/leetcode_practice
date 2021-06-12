# My solution, also good solution(greedy+heap)
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations.append([target,0])
        ans=0
        fuel_heap=[]
        for i,j in stations:
            while startFuel<i:# 油不夠
                if len(fuel_heap)==0:# 沒油加
                    return(-1)
                add_fuel=-1*heapq.heappop(fuel_heap)# 取出最大的
                ans+=1
                startFuel+=add_fuel
            heapq.heappush(fuel_heap,-j)# 不管油夠不夠
        return(ans)
#%% DP solution(slow)
class Solution(object):
    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in xrange(i, -1, -1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)

        for i, d in enumerate(dp):
            if d >= target: return i
        return -1