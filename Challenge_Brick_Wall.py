# TLE answer
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        through=[len(wall)]*(sum(wall[0]))
        for i in range(len(wall)):
        #    print('i',i)
            cur_brick=0
            for j in wall[i]:
        #        print('j',j)
                cur_brick+=j
        #        print('curbruick',cur_brick)
                through[cur_brick-1]-=1
        ans=min(through[:-1]) if through[:-1] else len(wall)
        return(ans)
#%% Accepted but slow answer
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        through=collections.defaultdict(int)
        for i in range(len(wall)):
            cur_brick=0
            for j in wall[i]:
                cur_brick+=j
                if cur_brick!=sum(wall[0]):
                    through[cur_brick-1]-=1
        if through:
            return(min(list(through.values()))+len(wall))
        else:
            return(len(wall))
#%% Elegant answer
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        dic = collections.defaultdict(int)
        
        for row in wall:
            cur_sum = 0
            for brick in row[:-1]:
                cur_sum += brick
                dic[cur_sum] += 1
        return len(wall) - max(dic.values(),default=0)
#%% Revised answer
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        through=collections.defaultdict(int)
        for i in range(len(wall)):
            cur_brick=0
            for j in wall[i][:-1]:
                cur_brick+=j
                through[cur_brick-1]-=1
        if through:
            return(min(list(through.values()))+len(wall))
        else:
            return(len(wall))