# My solution(slow)
class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(a) for a in n)
#%% 3X faster
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))
#%% 2X faster than above
class Solution:
    def minPartitions(self, n: str) -> int:
        for num in range(9,-1, -1):
            if str(num) in n:
                return num
#%% Faster
class Solution:
    def minPartitions(self, n: str) -> int:
        if '9' in n:
            return 9
        if '8' in n:
            return 8
        if '7' in n:
            return 7
        if '6' in n:
            return 6
        if '5' in n:
            return 5
        if '4' in n:
            return 4
        if '3' in n:
            return 3
        if '2' in n:
            return 2
        if '1' in n:
            return 1
#%% Fast like int(max(n)) approash
class Solution:
    def minPartitions(self, n: str) -> int:
        numbers = set(n)
        return max(numbers)