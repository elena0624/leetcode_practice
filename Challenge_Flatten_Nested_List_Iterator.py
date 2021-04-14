# My solution
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList=nestedList      
    
    def next(self) -> int:
        return self.nestedList.pop(0).getInteger()
    
    def hasNext(self) -> bool:
        if not self.nestedList:
            return False
        while self.nestedList:# 如果nestedlist裡面還有東西
            pop_item = self.nestedList.pop(0)
            if pop_item.isInteger():
                self.nestedList=[pop_item]+self.nestedList
                return True    
            elif pop_item.getList():
                while pop_item.getList():
                    pop_item2=pop_item.getList().pop()
                    if pop_item2.isInteger or pop_item2.getList():
                        self.nestedList=[pop_item2]+self.nestedList
                if self.nestedList[0].isInteger():
                    return True
        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

#%% Others solutions
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nested_list: [NestedInteger]):
        self.count=0
        self.flat_list=[]
        self._flatten(nested_list)
        self.n=len(self.flat_list)
    def _flatten(self, nested_list):
        for sublist in nested_list:
            if sublist.isInteger():
                self.flat_list.append(sublist.getInteger())
            else:
                self._flatten(sublist.getList())
                
    def next(self) -> int:
        while self.hasNext():
            self.count+=1
            return self.flat_list[self.count-1]
    
    def hasNext(self) -> bool:
        if self.count<self.n:
            return True
        else:
            return False
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
#%%
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = nestedList[::-1]
        
    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop().getInteger()
        
    def hasNext(self):
        """
        :rtype: bool
        """
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1]
        return False
