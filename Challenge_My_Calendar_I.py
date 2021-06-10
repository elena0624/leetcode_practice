# MY first code
import bisect
class MyCalendar:

    def __init__(self):
        self.intervals=[]
        self.len_intervals=0

    def book(self, start: int, end: int) -> bool:
        x = bisect.bisect(self.intervals, (start,end))
        if x>0 and self.intervals[x-1][0]==start:# 如果有重複的 insert的位置會是重複的下一個 所以看前面那個是不是一樣 一樣不行 start不能重複
            return(False)
        elif x>0 and self.intervals[x-1][1]>start:# 如果這不是第一個 那前面那個end不能比這個start晚
            return(False)
        elif x<self.len_intervals and self.intervals[x][0]<end:# 如果這不是最後一個 那後面的start不能比這個end還早
            return(False)
        else:#else:# 可以 那就輸入
            self.intervals=self.intervals[:x]+[(start,end)]+self.intervals[x:]
            self.len_intervals+=1
            return(True)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
#%% Elegant code
class MyCalendar:
    def __init__(self):
        self.intervals = []
    
    def book(self, start: int, end: int) -> bool:
        if end <= start:
            return False
        i = bisect.bisect_right(self.intervals, start)
        if i % 2:#聰明啊! 因為它把start跟end都擺在一起，如果正常的話一定是輸入到end的後面就是單數 如果輸入到start後面就是雙數=> 這個檢查start是不是在別人的start跟end中間
        # start is in some stored interval
            return False
        j = bisect.bisect_left(self.intervals, end)
        if i != j:# 這個檢查start跟end有沒有包夾到其他interval
            return False
        self.intervals[i:i] = [start, end]# 學到新用法了!!!這就是從i開始改成後面list的內容，但後面的仍為保存
        return True

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
#%% Approach #1: Brute Force [Accepted]
class MyCalendar(object):
    def __init__(self):
        self.calendar = []

    def book(self, start, end):
        for s, e in self.calendar:
            if s < end and start < e:
                return False
        self.calendar.append((start, end))
        return True
#%% Approach #2: Balanced Tree [Accepted]
class Node:
    __slots__ = 'start', 'end', 'left', 'right'
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True
            return self.right.insert(node)
        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True
            return self.left.insert(node)
        else:
            return False

class MyCalendar(object):
    def __init__(self):
        self.root = None

    def book(self, start, end):
        if self.root is None:
            self.root = Node(start, end)
            return True
        return self.root.insert(Node(start, end))
#%% Other code
class MyCalendar:

    def __init__(self):
        self.starts = []
        self.ends = []

    def book(self, start: int, end: int) -> bool:
        index = bisect.bisect(self.ends, start)
        if index == len(self.ends) or end<=self.starts[index]:
            self.starts.insert(index, start)
            self.ends.insert(index, end)
            return True
        return False

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
#%% My revised code not using bisect
class MyCalendar(object):
    def __init__(self):
        self.s_l = []
        self.e_l = []
    def book(self, start, end):
        l=0
        r=len(self.e_l)
        while l<r:
            m=(l+r)//2
            if start>=self.e_l[m]:
                l=m+1
            else:
                r=m
        if r==len(self.e_l) or self.s_l[r]>=end:
            self.s_l.insert(r,start)
            self.e_l.insert(r,end)
            return(True)
        else:
            return(False)