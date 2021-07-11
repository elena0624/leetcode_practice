# My solution. Not fast enough
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ls=[]
        self.len=0
        
    def addNum(self, num: int) -> None:
        self.len+=1
        bisect.insort_left(self.ls,num)

    def findMedian(self) -> float:
        if self.len%2==0:
            return (self.ls[self.len//2]+self.ls[self.len//2-1])/2
        else:
            return self.ls[self.len//2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
#%% Recommended solution
class MedianFinder:
    def __init__(self):
        self.small = []  # the smaller half of the list, max heap (invert min-heap)
        self.large = []  # the larger half of the list, min heap

    def addNum(self, num):
        if len(self.small) == len(self.large):
            # 兩堆一樣多的時候就往大的塞，所以先塞小的之後把"最大的"pop出來塞到大的
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            # 大堆比較多的時候塞到小堆，所以把它塞到大堆之後把"最小的"弄出來塞到小堆
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self):
        if len(self.small) == len(self.large):
        # -是因為小堆要取最大值，所以是用負值存
            return float(self.large[0] - self.small[0]) / 2.0
        else:
            return float(self.large[0])
